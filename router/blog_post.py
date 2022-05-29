from typing import Dict, List, Optional
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    num_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "val1"}
    image: Optional[Image] = None


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None,
        title="Id of the comment",
        description="Some description for comment_id",
        alias="commentId",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
):
    return {"blog": blog, "id": id, "comment_id": comment_id, "content": content}


def required_functionality():
    return {"message": "Learning FastAPI is important."}
