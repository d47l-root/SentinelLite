from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, engine
from app.models.log_entry import LogEntry
from app.models.alert import Alert
from app.api.ingestion import router as ingestion_router
from app.api.alerts import router as alerts_router


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(ingestion_router)
app.include_router(alerts_router)


@app.get("/health")
def health_check():
    return {"status":"alive","app_name":settings.app_name,"debug": settings.debug}
