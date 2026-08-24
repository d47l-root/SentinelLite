from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.ingestion import get_db
from app.models.alert import Alert

router = APIRouter()

@router.get("/alerts")
def list_alerts(db: Session = Depends(get_db)):
    return db.query(Alert).all()