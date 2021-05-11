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

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class Token(BaseModel):
    access_token: str
    token_type: str
    user: Optional[User] = None

class TokenData(BaseModel):
    username: Optional[str] = None

class UserInDB(User):
    hashed_password: str