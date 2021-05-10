from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum

app = FastAPI()

#Choices
class ModelChoices(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#DTO
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/model/{model_name}")
def get_model(model_name=ModelChoices):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, **item.dict()}