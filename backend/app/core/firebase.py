import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import auth

# 🔑 Load env FIRST
load_dotenv()

FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")

if not FIREBASE_PROJECT_ID:
    raise RuntimeError("FIREBASE_PROJECT_ID is not set")

# Initialize Firebase Admin only once
if not firebase_admin._apps:
    firebase_admin.initialize_app()

def verify_firebase_token(id_token: str):
    decoded_token = auth.verify_id_token(id_token)
    return decoded_token
