💳 M-Pesa Payment Frontend
A full-stack M-Pesa payment application built with FastAPI, Bootstrap 5, and JavaScript. Users can enter their phone number and amount to receive an STK Push prompt directly on their phone.

✨ Features
💸 STK Push Integration – Trigger M-Pesa payment prompts from a web interface

🎨 Bootstrap 5 UI – Clean, responsive, mobile-friendly design

⚡ Real-time Feedback – Instant status updates via JavaScript

🔄 Callback Handling – Receives payment confirmations from M-Pesa

🔐 Environment Variables – Keeps credentials secure

📱 Mobile-First – Works perfectly on phones and desktops

🛠️ Tech Stack
Backend: FastAPI, Python 3.8+

Frontend: HTML5, Bootstrap 5, JavaScript (Fetch API)

HTTP Client: Requests

Templating: Jinja2

Server: Uvicorn

📁 Project Structure
text
mpesa-payment-frontend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes + HTML serving
│   ├── config.py        # Environment configuration
│   ├── mpesa.py         # M-Pesa API logic
│   └── models.py        # Pydantic models
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
├── templates/
│   └── index.html       # Payment form UI
├── .env                 # Secrets (not committed)
├── .env.example         # Template for secrets
├── .gitignore
├── requirements.txt
└── README.md
🚀 Quick Start
1. Clone the repository
bash
git clone https://github.com/asundah/mpesa-payment-frontend.git
cd mpesa-payment-frontend
2. Create and activate a virtual environment
bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Configure environment variables
bash
cp .env.example .env
Edit .env with your M-Pesa sandbox credentials:

env
CONSUMER_KEY=your_consumer_key_here
CONSUMER_SECRET=your_consumer_secret_here
SHORTCODE=174379
PASSKEY=your_passkey_here
ENVIRONMENT=sandbox
CALLBACK_URL=https://your-ngrok-url.ngrok-free.dev/api/callback
5. Expose your local server with ngrok
bash
ngrok http 8000
Copy the generated HTTPS URL and update CALLBACK_URL in .env.

6. Run the server
bash
uvicorn app.main:app --reload
7. Open in browser
text
http://localhost:8000
📡 API Endpoints
Method	Endpoint	Description
GET	/	Payment form (HTML)
POST	/api/initiate-payment	Trigger STK Push
POST	/api/callback	M-Pesa callback receiver
GET	/api/status	API health status
GET	/docs	Swagger UI (dev only)
🧪 Testing the Payment Flow
Open http://localhost:8000

Enter a phone number (e.g., 254708374149)

Enter amount (e.g., 1)

Click Pay Now

Check your phone for the M-Pesa prompt

Enter your PIN to confirm

Watch the ngrok terminal for the callback

🔐 Environment Variables
Variable	Description
CONSUMER_KEY	M-Pesa API consumer key
CONSUMER_SECRET	M-Pesa API consumer secret
SHORTCODE	Paybill/Till number (sandbox: 174379)
PASSKEY	Lipa Na M-Pesa passkey
ENVIRONMENT	sandbox or production
CALLBACK_URL	Public URL for M-Pesa callbacks
⚠️ Important Notes
Never commit .env – it contains secrets.

ngrok URL changes on restart – update .env each time.

Sandbox does not send real SMS – use test numbers.

Disable /docs in production for security.

📄 License
MIT License

👨‍💻 Author
Amos Asunda
GitHub: @asundah
