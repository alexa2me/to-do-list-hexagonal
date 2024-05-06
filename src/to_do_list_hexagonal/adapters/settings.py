import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings as PydanticBaseSettings

load_dotenv()


class BaseSettings(PydanticBaseSettings):
    PROJECT_NAME: str = "to_do_list_hexagonal"

    # MySQL
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_SCHEMA: str = os.getenv("DB_SCHEMA", "")
    DB_PORT: str = os.getenv("DB_PORT", "")
    DB_URL: str = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = BaseSettings()
