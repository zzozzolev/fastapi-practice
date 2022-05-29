from fastapi import FastAPI
from router import blog_get, blog_post
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

models.Base.metadata.create_all(engine)
