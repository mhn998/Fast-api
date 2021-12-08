from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm.session import Session
from ..models import Blog_model
from ..database import get_db
from ..schemas import Blog_schema


def get_all(db: Session):
    blogs = db.query(Blog_model).all(
    )
    return blogs


def show(id: int, response, db: Session):
    blog = db.query(Blog_model).filter(Blog_model.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Blog with the id {id} not found"}
    return blog


def create(request, db: Session):
    new_blog = Blog_model(title=request.title,
                          body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(Blog_model).filter(Blog_model.id ==
                                       id).delete(synchronize_session=False)

    db.commit()
    return {"details": "Done!"}


def update(id: int, request, db: Session):
    blog = db.query(Blog_model).filter(Blog_model.id ==
                                       id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated'
