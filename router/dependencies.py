from fastapi import APIRouter, Depends
from fastapi.requests import Request

router = APIRouter(prefix="/dependencies", tags=["dependencies"])


def convert_headers(request: Request, separator: str = "--"):
    return [f"{k} -- {v}" for k, v in request.headers.items()]


@router.get("")
def get_items(headers=Depends(convert_headers)):
    return {"items": ["a", "b", "c"], "headers": headers}


@router.post("/new")
def get_items(headers=Depends(convert_headers)):
    return {"result": "new item created", "headers": headers}


class Account:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


@router.post("/user")
def create_user(name: str, email: str, password: str, account: Account = Depends()):
    return {"name": account.name, "email": account.email}
