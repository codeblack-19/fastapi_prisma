from fastapi import APIRouter, Depends
from db.db_session import db_session
from schemas.author import AuthorIn, AuthorOut
from typing import List
from prisma import Prisma

author_router = APIRouter()

@author_router.get("/", response_model=List[AuthorOut])
async def get_all(db: Prisma = Depends(db_session)):
    author = await db.author.find_many()
    return author

@author_router.post("/", response_model=AuthorOut)
async def create_author(author: AuthorIn, db: Prisma = Depends(db_session)):
    author = await db.author.create(data=author.model_dump())
    return author

@author_router.put("/{id}", response_model=AuthorOut)
async def update_author(id: int, author: AuthorIn, db: Prisma = Depends(db_session)):
    author = await db.author.update(
        where={"id": id},
        data=author.model_dump()
    )
    return author

@author_router.delete("/")
async def delete_author(id: int, db: Prisma = Depends(db_session)):
    author = await db.author.delete(where={"id": id})
    return author