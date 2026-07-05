from pydantic import BaseModel


class BlogPost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]
