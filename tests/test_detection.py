from app.models.log_entry import LogEntry
from app.detection.rules import detect_failed_login

def test_detect_failed_login_matches():
    log = LogEntry(source="auth-server", message="User admin failed login attempt")
    result = detect_failed_login(log)
    assert result == "Possible failed login attempt detected"

def test_detect_failed_login_no_match():
    log = LogEntry(source="web-server", message="User admin logged in successfully")
    result = detect_failed_login(log)
    assert result is None