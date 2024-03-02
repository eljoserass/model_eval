from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import MySQLDsn, HttpUrl, AnyUrl, field_validator, EmailStr

class Settings(BaseSettings):
    POE_API_TOKEN: str
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
