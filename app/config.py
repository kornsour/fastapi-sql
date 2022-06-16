import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

# Cache the settings so get_settings is only called once
@lru_cache()
def get_settings() -> BaseSettings:
    # Can simply declare handler as asynchronous with 'async'
    # As long as no blocking I/O calls in the handler
    log.info("Loading config settings from the environment...")
    return Settings()