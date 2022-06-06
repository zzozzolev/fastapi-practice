from urllib.request import Request
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import blog_get, blog_post, user, article, product
from auth import authentication
from db import models
from db.database import engine

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"detail": exc.name}
    )


models.Base.metadata.create_all(engine)
