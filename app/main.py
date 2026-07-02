from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from datetime import datetime


class BlogPost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]


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
    if len(posts) >= 0:
        return posts


@app.put("/posts/{post_id}", status_code=200)
async def update_blog_post(post_id: int, blog_post: BlogPost, response: Response):
    target = None
    for post in posts:
        if post.get("id") == post_id:
            target = post
            break

    if target is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Post not found"}

    target["title"] = blog_post.title
    target["content"] = blog_post.content
    target["category"] = blog_post.category
    target["tags"] = blog_post.tags
    target["updatedAt"] = datetime.now()

    return target


@app.delete("/posts/{post_id}", status_code=204)
async def delete_blog_post(post_id: int, response: Response):
    target = None
    for post in posts:
        if post.get("id") == post_id:
            target = post
            break
    if target:
        posts.remove(target)
        return

    response.status_code = status.HTTP_404_NOT_FOUND
