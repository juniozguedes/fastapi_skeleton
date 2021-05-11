from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from typing import Optional, Set

from fastapi import FastAPI, Query, Depends, HTTPException, status
from pydantic import BaseModel

from routes import items, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(items.router)
