from pathlib import Path
from pydantic import BaseModel, AnyHttpUrl


BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 1


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"
    auth_jwt: AuthJWT = AuthJWT()
    pg_db_url = AnyHttpUrl
    api_key: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
