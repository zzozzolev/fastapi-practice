from typing import Optional
from fastapi import APIRouter, status, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]


@router.get("/all")
def get_all_product():
    # return products
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get("/withheader")
def get_products(response: Response, custom_header: Optional[list[str]] = Header(None)):
    response.headers["custom_response_header"] = ", ".join(custom_header)
    return products


@router.get(
    "/{id}",
    responses={
        status.HTTP_200_OK: {
            "content": {"text/html": {"example": "<div>product</div>"}},
            "description": "Returns the HTML for an object",
        },
        status.HTTP_404_NOT_FOUND: {
            "content": {"text/plain": {"example": "Product not available"}},
            "description": "A cleartext error message",
        },
    },
)
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(
            status_code=status.HTTP_404_NOT_FOUND, content=out, media_type="text/plain"
        )
    else:
        product = products[id]
        out = f"""
        <head>
        <style>
        .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>
        </head>
        <div class="product">{product}</div>
        """
    return HTMLResponse(content=out, media_type="text/html")
