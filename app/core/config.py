from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Property Manager API"
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "changeme"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
