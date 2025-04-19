import jwt
from core.config import settings
import bcrypt


def encode_jwt(
        payload: dict,
        privet_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm:str = settings.auth_jwt.algorithm
    ):
    return jwt.encode(payload=payload, key=privet_key, algorithm=algorithm)


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
    ):
    return jwt.decode(token=token, key=public_key, algorithms=[algorithm])


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
