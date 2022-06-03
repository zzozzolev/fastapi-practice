from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from exceptions import StoryException
from schemas import ArticleBase, ArticleDisplay
from db.database import get_db
from db import db_article

router = APIRouter(prefix="/article", tags=["article"])

# Create article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please.")

    return db_article.create_article(db, request)


# Get specific article
@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    article = db_article.get_article(db, id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {id} not found.",
        )

    return article
