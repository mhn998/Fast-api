from fastapi import FastAPI
from typing import Optional
from blog.schemas import Blog_schema
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'blog published list up to {limit}'}
    else:
        return {'data': 'published list from the db'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished'}


@app.post('/blog')
def create_blog(blog: Blog_schema):
    return {'data': f'Blog is created for {blog.title}'}


# for debugging purpose
# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)
