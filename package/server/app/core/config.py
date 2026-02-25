from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App info
    PROJECT_NAME: str = "Fitness Booking API"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database parts
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str
    TEST_DB_URL: str = "sqlite+aiosqlite:///:memory:"

    # Full database URL (computed from parts)
    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+asyncmy://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Pydantic V2 model_config to load .env
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


# Global instance
settings = Settings()