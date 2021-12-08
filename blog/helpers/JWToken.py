from os import getenv
from typing import Optional
from dotenv import load_dotenv
from datetime import timedelta, datetime
from jose import jwt, JWTError
from ..schemas import TokenData

load_dotenv()
SECRET_KEY = getenv('SECRET_KEY')
ALGORTHIM = getenv('ALGORITHIM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
print(ACCESS_TOKEN_EXPIRE_MINUTES)
print(type(ACCESS_TOKEN_EXPIRE_MINUTES))


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORTHIM)
    return encode_jwt


def verify_token(token: str, credintials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORTHIM])
        email: str = payload.get("sub")
        if email is None:
            raise credintials_exception

        token_data = TokenData(email=email)

    except JWTError:
        raise credintials_exception
