from sqlalchemy.orm import Session
from app.models.log_entry import LogEntry
from app.models.alert import Alert
from app.detection.rules import detect_failed_login

RULES = [detect_failed_login]

def run_detection(log: LogEntry, db: Session) -> list[Alert]:
    created_alerts = []
    for rule in RULES:
        result = rule(log)
        if result is not None:
            alert = Alert(description=result, severity="medium", log_id=log.id)
            db.add(alert)
            created_alerts.append(alert)
    db.commit()
    return created_alerts