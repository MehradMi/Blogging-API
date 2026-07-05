from fastapi import APIRouter, Response, status
from datetime import datetime
from app.schemas import BlogPost

router = APIRouter(prefix="/posts", tags=["posts"])

posts = []


def find_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@router.post("/", status_code=201)
async def create_blog_post(blog_post: BlogPost):

    new_post = {
        "id": len(posts) + 1,
        **blog_post.model_dump(),
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
    }

    posts.append(new_post)

    return new_post


@router.get("/{post_id}", status_code=200)
async def read_blog_post(post_id: int, response: Response):
    target = find_post(post_id)
    if target is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Post not found"}

    return target


@router.get("/", status_code=200)
async def read_all_blog_posts():
    return posts


@router.put("/{post_id}", status_code=200)
async def update_blog_post(post_id: int, blog_post: BlogPost, response: Response):
    target = find_post(post_id)
    if target is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Post not found"}

    target["title"] = blog_post.title
    target["content"] = blog_post.content
    target["category"] = blog_post.category
    target["tags"] = blog_post.tags
    target["updatedAt"] = datetime.now()

    return target


@router.delete("/{post_id}", status_code=204)
async def delete_blog_post(post_id: int, response: Response):
    target = find_post(post_id)
    if target is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Post not found"}

    posts.remove(target)
