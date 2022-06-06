from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from exceptions import StoryException
from schemas import ArticleBase, ArticleDisplay, UserBase
from db.database import get_db
from db import db_article
from auth.oauth2 import get_current_user

router = APIRouter(prefix="/article", tags=["article"])

# Create article
@router.post("/", response_model=ArticleDisplay)
def create_article(
    request: ArticleBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please.")

    return db_article.create_article(db, request)


# Get specific article
@router.get("/{id}")  # , response_model=ArticleDisplay)
def get_article(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    article = db_article.get_article(db, id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {id} not found.",
        )

    return {"data": article, "current_user": current_user}
