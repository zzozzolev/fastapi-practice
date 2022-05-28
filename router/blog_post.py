from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    num_comments: int


@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}
