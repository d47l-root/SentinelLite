from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from app.db.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    log_id = Column(Integer, ForeignKey("logs.id"))
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))