from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: str = "sqlite:///./adidas_store.db"
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    environment: str = "development"
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"

settings = Settings()