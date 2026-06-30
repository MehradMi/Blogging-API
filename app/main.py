from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from datetime import datetime

from starlette.status import HTTP_404_NOT_FOUND


class BlogPost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]


class BlogPostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str]
    createdAt: datetime
    updatedAt: datetime


app = FastAPI()

posts = []


@app.post("/posts/", status_code=201)
async def create_blog_post(blog_post: BlogPost):

    new_post = {
        "id": len(posts) + 1,
        **blog_post.model_dump(),
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
    }

    posts.append(new_post)

    return new_post


@app.get("/posts/{post_id}", status_code=200)
async def read_blog_post(post_id: int, response: Response):
    for post in posts:
        if post.get("id") == post_id:
            return post

    response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/posts/", status_code=200)
async def read_all_blog_posts():
    if len(posts) > 0:
        return posts


@app.delete("/posts/{post_id}", status_code=204)
async def delete_blog_post(post_id: int, response: Response):
    for post in posts:
        if post.get("id") == post_id:
            posts.remove(post)
            return
    response.status_code = status.HTTP_404_NOT_FOUND
