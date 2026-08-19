from pydantic import BaseModel

class LogEntryCreate(BaseModel):
   source: str
   message: str
