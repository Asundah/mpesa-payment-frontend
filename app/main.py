from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from .models import PaymentRequest, PaymentResponse
from .mpesa import MpesaAPI
import os

app = FastAPI(
    title="M-Pesa Payment App",
    description="M-Pesa STK Push with HTML Frontend"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Initialize M-Pesa API
mpesa = MpesaAPI()

# ============================================
# HTML ROUTES
# ============================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the payment page"""
    return templates.TemplateResponse(
        request, "index.html",
        {"title": "M-Pesa Payment"}
    )

# ============================================
# API ROUTES
# ============================================

@app.post("/api/initiate-payment")
async def initiate_payment(request: PaymentRequest):
    """Initiate STK Push payment"""
    result = mpesa.stk_push(
        phone_number=request.phone_number,
        amount=request.amount,
        account_reference=request.account_reference,
        transaction_desc=request.transaction_desc
    )
    
    if result.get("ResponseCode") == "0":
        return {
            "status": "success",
            "message": "STK Push sent successfully. Check your phone.",
            "checkout_request_id": result.get("CheckoutRequestID")
        }
    else:
        return {
            "status": "failed",
            "message": result.get("ResponseDescription", "Payment failed"),
            "checkout_request_id": None
        }

@app.post("/api/callback")
async def mpesa_callback(request: Request):
    """Handle M-Pesa callback"""
    data = await request.json()
    
    body = data.get("Body", {})
    stk_callback = body.get("stkCallback", {})
    
    result_code = stk_callback.get("ResultCode")
    result_desc = stk_callback.get("ResultDesc")
    checkout_request_id = stk_callback.get("CheckoutRequestID")
    
    if result_code == 0:
        print(f"✅ Payment successful! CheckoutRequestID: {checkout_request_id}")
    else:
        print(f"❌ Payment failed: {result_desc}")
    
    return JSONResponse(
        content={"ResultCode": 0, "ResultDesc": "Success"},
        status_code=200
    )

@app.get("/api/status")
async def get_status():
    """Check API status"""
    return {"status": "online", "message": "M-Pesa API is running"}

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": os.getenv("ENVIRONMENT", "sandbox")}