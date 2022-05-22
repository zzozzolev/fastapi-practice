from enum import Enum
from fastapi import FastAPI, Response, status

app = FastAPI()


# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs provided."}


@app.get("/blog/all")
def get_all_blogs(page, page_size):
    return {"message": f"All {page_size} blogs on page {page}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_all_blogs(type: BlogType):
    return {"message": f"Blog type {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found."}
    else:
        return {"message": f"Blog with id {id}."}
