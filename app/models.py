from pydantic import BaseModel
from typing import Optional

class PaymentRequest(BaseModel):
    amount: float
    phone_number: str
    account_reference: str = "Order 123"
    transaction_desc: str = "Payment"

class PaymentResponse(BaseModel):
    status: str
    message: str
    checkout_request_id: Optional[str] = None