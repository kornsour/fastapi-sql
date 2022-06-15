'''Main application file'''

from fastapi import FastAPI

from app.config import get_settings, Settings

app = FastAPI()

@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }