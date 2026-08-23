from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.db.database import SessionLocal
from app.models.log_entry import LogEntry
from app.schemas.log_entry import LogEntryCreate
from app.detection.engine import run_detection


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        
@router.post("/logs")
def create_log(log: LogEntryCreate, db: Session = Depends(get_db)):
    new_log = LogEntry(source=log.source, message=log.message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    run_detection(new_log, db)
    db.refresh(new_log)
    return new_log