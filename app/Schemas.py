from pydantic import BaseModel,EmailStr, Field,conint
from datetime import datetime
from typing import Annotated, Optional
class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass 
class PostUpdate(PostBase):
    pass
class PostResponse(PostBase):
    id:int
    owner:CreationResponse
    created_at:datetime

    class Config:
        from_attributes=True
class Creation(BaseModel):
    username:str
    email:EmailStr
    password:str
class CreationResponse(BaseModel):
    username:str
    email:EmailStr
    id:int
    created_at:datetime
class PostOut(BaseModel):
    Post: PostResponse
    likes: int

    class Config:
        from_attributes = True
class Login(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str 
class TokenData(BaseModel):
    id:Optional[int]=None
class Vote(BaseModel):
    post_id:int 
    dir: Annotated[int, Field(ge=0, le=1)]