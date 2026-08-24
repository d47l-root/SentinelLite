from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.ingestion import get_db
from app.models.alert import Alert
from app.core.security import verify_credentials

router = APIRouter()

@router.get("/alerts")
def list_alerts(db: Session = Depends(get_db), user: str = Depends(verify_credentials)):
    return db.query(Alert).all()