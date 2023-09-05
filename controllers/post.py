from fastapi import APIRouter, Depends
from db.db_session import db_session
from prisma import Prisma
from schemas.post import PostIn, PostOut
from typing import List

post_router = APIRouter()

@post_router.get("/", response_model=List[PostOut])
async def get_all(db: Prisma = Depends(db_session)):
    return await db.post.find_many(
        include={
            "author": True
        }
    )

@post_router.post("/", response_model=PostOut)
async def create_post(post: PostIn, db: Prisma = Depends(db_session)):
    return await db.post.create(data=post.model_dump())

@post_router.put("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostIn, db: Prisma = Depends(db_session)):
    return await db.post.update(
        where={"id": id},
        data=post.model_dump()
    )
