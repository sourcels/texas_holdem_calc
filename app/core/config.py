from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    host: str = Field("127.0.0.1", env="HOST")
    port: int = Field(8000, env="PORT")
    debug: bool = Field(True, env="DEBUG")
    reload: bool = Field(True, env="RELOAD")

    database_url: str = Field(..., env="DATABASE_URL")  # required

    max_players: int = Field(9, env="MAX_PLAYERS")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()