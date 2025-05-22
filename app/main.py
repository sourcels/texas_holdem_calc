from fastapi import FastAPI
from config import load_uvicorn
import uvicorn


app = FastAPI(title="Texas Hold'em Calculator")

if __name__ == "__main__":
    payload = load_uvicorn()
    uvicorn.run(
        app=payload["app"],
        host=payload["host"],
        port=payload["port"],
        reload=payload["reload"],
        log_level=payload["log_level"],
        workers=payload["workers"]
    )