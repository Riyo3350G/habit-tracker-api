# Security utilities for the application
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str) -> str:
    "Hashing the pasword string"
    return password_context.hash(password)

def verify_password(entered_password: str, stored_password: str) -> bool:
    "Verifying the entered password with the stored password"
    return password_context.verify(entered_password, stored_password)

# JWT configuration
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    "Creating a JWT access token"
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

