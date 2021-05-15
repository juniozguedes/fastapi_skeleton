from fastapi import APIRouter
from .dtos import Image, Item
from typing import Optional, Set
from fastapi import FastAPI, Query, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None, max_length=4)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@router.post("/items/")
async def create_item(item: Item):
    return item

@router.put("/items/{item_id}")
async def update_item(
    item_id: int,
    q: Optional[str] = None,
    item: Optional[Item] = None,
):  
    results = {"Jedi_master":item.name, "item_id":item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update(**item.dict())
    return results