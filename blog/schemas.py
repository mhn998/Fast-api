from typing import List, Optional
from pydantic import BaseModel

from blog.database import Base


class Blog_schema(BaseModel):
    title: str
    body: str
    published: Optional[bool]

    class Config():
        orm_mode = True


class User_schema (BaseModel):
    name: str
    email: str
    password: str


class Show_user(BaseModel):
    name: str
    email: str
    blogs: List[Blog_schema] = []

    class Config():
        orm_mode = True


class Show_user_without_pass(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Blog_show(BaseModel):
    title: str
    body: str
    creator: Show_user_without_pass
    # this will remove id from the response when we pass this schema as a response model

    class Config():
        orm_mode = True


class Blogs_all(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True
