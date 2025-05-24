from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8800, env="PORT")
    reload: bool = Field(False, env="RELOAD")
    log_level: str = Field("info", env="LOG_LEVEL")
    workers: int = Field(1, env="WORKERS")

    jwt_secret: str = Field(..., env="JWT_SECRET")
    jwt_expires_min: int = Field(180, env="JWT_EXPIRES_MIN")

    minio_host: str = Field(..., env="MINIO_HOST")
    minio_bucket: str = Field("poker_users", env="MINIO_BUCKET")
    minio_access_key: str = Field(..., env="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(..., env="MINIO_SECRET_KEY")
    minio_secure: bool = Field(True, env="MINIO_SECURE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()