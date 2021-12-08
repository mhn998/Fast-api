from os import stat
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from starlette.routing import request_response
# from ..JWToken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from ..helpers.JWToken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from ..schemas import Login
from ..database import get_db
from ..models import User_model
from ..helpers.hashing import Hash
from datetime import timedelta


router = APIRouter(tags=['authentication'], prefix='/api/v2/login')


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User_model).filter(
        User_model.email == request.username).first()

    # check if the user exists in the first place
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credintials")

    # check if the password is correct
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")

    # generate JWT access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
