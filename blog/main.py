from .database import engine
from .models import Base
import uvicorn
from fastapi import FastAPI
from .routers import blogs, users, auth


app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(auth.router)
Base.metadata.create_all(engine)


# All logic starts from here (main) , then we seperate them into two routes with prefix and tags , after routes are done we seperate the logic for route handlers in a

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/blog', status_code=status.HTTP_201_CREATED)
# def create(request: Blog_schema, db: Session = Depends(get_db)):
#     new_blog = Blog_model(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model=List[Blog_show])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(Blog_model).all(
#     )
#     return blogs


# @app.get('/blog/{id}', status_code=200, response_model=Blog_show, tags=['blogs'])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(Blog_model).filter(Blog_model.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id {id} not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"details": f"Blog with the id {id} not found"}
#     return blog


# @app.delete('/blog/{id}')
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(Blog_model).filter(Blog_model.id ==
#                                        id).delete(synchronize_session=False)

#     db.commit()
#     return {"details": "Done!"}


# @app.put("/blog/{id}")
# def update(id, request: Blog_schema, db: Session = Depends(get_db)):
#     print(type(request))
#     blog = db.query(Blog_model).filter(Blog_model.id ==
#                                        id)

#     # print(blog)
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

#     blog.update(request.dict(), synchronize_session=False)
#     db.commit()
#     return 'updated'


# @app.post('/user', response_model=Show_user)
# def create_user(request: User_schema, db: Session = Depends(get_db)):
#     pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#     new_user = User_model(name=request.name, email=request.email,
#                           password=pwd_context.hash(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/users', response_model=List[Show_user])
# def get_all_users(db: Session = Depends(get_db)):
#     users = db.query(User_model).all()
#     return users


# @app.get('/user/{id}', response_model=Show_user)
# def get_user(id: int, db: Session = Depends(get_db)):

#     user = db.query(User_model).filter(User_model.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")

#     return user


# @app.delete('/user/{id}')
# def delete_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(User_model).filter(User_model.id == id)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     user.delete(synchronize_session=False)
#     db.commit()
#     return {f"user with {id} has been deleted Successfully!"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
