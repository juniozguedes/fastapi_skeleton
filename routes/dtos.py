from pydantic import BaseModel
from typing import Optional, Set

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    tags: Set[str] = set() #Unique items list
    image: Optional[Image] = None