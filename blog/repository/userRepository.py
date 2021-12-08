from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
from ..models import User_model
from sqlalchemy.orm import Session
from ..helpers.hashing import Hash


def create_user(request, db: Session):
    new_user = User_model(name=request.name, email=request.email,
                          password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    users = db.query(User_model).all()
    return users


def get_user(id: int, db: Session):

    user = db.query(User_model).filter(User_model.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user


def delete_user(id: int, db: Session):
    user = db.query(User_model).filter(User_model.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return {f"user with {id} has been deleted Successfully!"}
