from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"alive","app_name":settings.app_name,"debug": settings.debug}
