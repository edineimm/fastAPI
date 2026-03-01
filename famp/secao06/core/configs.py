from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

DBBaseModel = declarative_base()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"

    JWT_SECRET: str = 'pZa_jKl1NFaTrnvAGv7R7UnEkComl1zzIrvHXz7ycsw'
    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class Config:
        case_sensitive = True


settings = Settings()
