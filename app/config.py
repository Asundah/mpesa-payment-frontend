import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MPESA Credentials
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    SHORTCODE = os.getenv("SHORTCODE", "174379")  # Default to sandbox shortcode if not set
    PASSKEY = os.getenv("PASSKEY")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "sandbox")  # Sandbox or Production
    CALLBACK_URL = os.getenv("CALLBACK_URL")