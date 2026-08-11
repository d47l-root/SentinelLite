from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, engine
from app.models.log_entry import LogEntry
from app.models.alert import Alert

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"alive","app_name":settings.app_name,"debug": settings.debug}
