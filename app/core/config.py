from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8800, env="PORT")
    log_level: str = Field("info", env="LOG_LEVEL")
    workers: int = Field(2, env="WORKERS")
    jwt_secret: str = Field("0000", env="JWT_SECRET")
    database_url: str = Field(..., env="DATABASE_URL")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()