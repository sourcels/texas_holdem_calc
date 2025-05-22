import os
from dotenv import load_dotenv
from fastapi import FastAPI
from models import Config

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

def load_uvicorn() -> Config:
    payload = {
        "app": "main:app",
        "host": os.getenv("HOST", "0.0.0.0"),
        "port": int(os.getenv("PORT", 8800)),
        "reload": os.getenv("RELOAD", "False").lower() in ("true", "1", "yes"),
        "log_level": os.getenv("LOG_LEVEL", "info"),
        "workers": int(os.getenv("WORKERS", 1))
    }
    return payload