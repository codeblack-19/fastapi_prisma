from pydantic import BaseModel
from datetime import datetime
from .author import AuthorOut

class PostBase(BaseModel):
    id: int
    created_at: datetime
    author_id: int
    author: AuthorOut | None

class PostIn(BaseModel):
    title: str
    author_id: int
    content: str

class PostOut(PostBase):
    title: str
    content: str