from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_password: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

print(settings.database_hostname)
 