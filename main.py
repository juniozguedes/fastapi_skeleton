from fastapi.security import OAuth2PasswordBearer
from typing import Optional, Set

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#DTOs

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    tags: Set[str] = set() #Unique items list
    image: Optional[Image] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None, max_length=4)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    q: Optional[str] = None,
    item: Optional[Item] = None,
    user: Optional[User] = None
):  
    results = {"Jedi_master":item.name, "item_id":item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update(**item.dict())
    if user:
        results.update(**user.dict())
    return results