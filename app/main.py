from config import load_uvicorn
import uvicorn

if __name__ == "__main__":
    payload = load_uvicorn()
    uvicorn.run(
        app=payload.app,
        host=payload.host,
        port=payload.port,
        reload=payload.reload,
        log_level=payload.log_level,
        workers=payload.workers
    )