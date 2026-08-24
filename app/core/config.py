from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool
    api_username: str
    api_password: str
    class Config:
        env_file = ".env"

settings = Settings() 
