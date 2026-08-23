from app.models.log_entry import LogEntry

def detect_failed_login(log: LogEntry) -> str | None:
    if "failed login" in log.message.lower()  :

        return  "Possible failed login attempt detected"
    return None