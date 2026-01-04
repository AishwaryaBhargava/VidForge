import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")
    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "dev-secret")

settings = Settings()
