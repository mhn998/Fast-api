from fastapi import APIRouter, Depends, status, Response
from typing import List
from ..database import get_db
from ..schemas import Blog_show, Blog_schema, Blogs_all
from sqlalchemy.orm import Session
from ..repository import blogRepsitory


router = APIRouter(tags=['blogs'], prefix='/api/v2/blog')


@ router.get('/', response_model=List[Blogs_all])
def all(db: Session = Depends(get_db)):
    return blogRepsitory.get_all(db)


@ router.get('/{id}', status_code=200, response_model=Blog_show)
def show(id, response: Response, db: Session = Depends(get_db)):
    return blogRepsitory.show(id, response, db)


@ router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog_schema, db: Session = Depends(get_db)):
    return blogRepsitory.create(request, db)


@ router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db)):
    return blogRepsitory.destroy(id, db)


@ router.put("/{id}")
def update(id, request: Blog_schema, db: Session = Depends(get_db)):
    return blogRepsitory.update(id, request, db)
