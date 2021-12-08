from fastapi import APIRouter, Depends
from typing import List

from ..database import get_db
from ..schemas import Show_user, User_schema
from sqlalchemy.orm import Session
from ..repository import userRepository


router = APIRouter(tags=['user'], prefix='/api/v2/user')


@router.post('/', response_model=Show_user)
def create_user(request: User_schema, db: Session = Depends(get_db)):
    return userRepository.create_user(request, db)


@router.get('/', response_model=List[Show_user])
def get_all_users(db: Session = Depends(get_db)):
    return userRepository.get_all_users(db)


@router.get('/{id}', response_model=Show_user)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepository.get_user(id, db)


@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return userRepository.delete_user(id, db)
