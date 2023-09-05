from pydantic import BaseModel, EmailStr

class AuthorBase(BaseModel):
    id: int

class AuthorIn(BaseModel):
    name: str
    email: EmailStr

class AuthorOut(AuthorBase):
    name: str
    email: EmailStr