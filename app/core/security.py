from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.core.config import settings

security = HTTPBasic()

def verify_credentials(credentails: HTTPBasicCredentials=Depends(security)):
    if credentails.username != settings.api_username or credentails.password != settings.api_password:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid credentails",
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentails.username