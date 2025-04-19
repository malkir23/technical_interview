from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_path: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    algorithm: str = 'RS256'
    access_token_expire_minutes: int = 1


class Settings(BaseSettings):
    PG_DB_URL: str = ''

    class Config:
        env_file = BASE_DIR / '.env'

settings = Settings()
