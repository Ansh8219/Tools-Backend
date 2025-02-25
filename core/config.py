import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Tools")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "true").lower() == "true"
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")

    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()
