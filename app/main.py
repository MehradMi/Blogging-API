from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

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
		"updatedAt": datetime.now()
	}

	posts.append(new_post)

	return new_post