import os
from dotenv import load_dotenv
import uvicorn

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

app = "app.api:app"
host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", 8800))
reload = os.getenv("RELOAD", "False").lower() in ("true", "1", "yes")
log_level = os.getenv("LOG_LEVEL", "info")
workers = int(os.getenv("WORKERS", 1))

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=host,
        port=port,
        reload=reload,
        log_level=log_level,
        workers=workers
    )