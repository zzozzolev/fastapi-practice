from enum import Enum
from typing import Dict, Optional
from fastapi import APIRouter, Depends, Response, status

from router.blog_post import required_functionality

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs.",
    response_description="The list of available blogs.",
)
def get_all_blogs(
    page: Optional[int] = 1,
    page_size: Optional[int] = 5,
    req_parameter: Dict = Depends(required_functionality),
):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameter}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulates retrieving a comment of a blog.

    - **id** mandatory path parameter.
    - **comment_id** mandatory path parameter.
    - **valid** optional query paramter.
    - **username** optional query paramter.
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_all_blogs(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found."}
    else:
        return {"message": f"Blog with id {id}."}
