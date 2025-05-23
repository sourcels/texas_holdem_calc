from starlette.types import ASGIApp
from pydantic import BaseModel


class Config(BaseModel):
    app: ASGIApp
    host: str
    port: int
    reload: str
    log_level: str
    workers: int