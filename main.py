from fastapi import FastAPI
from fastapi import Depends
from db.db_session import db_session
from controllers import (
    author, post
)


app = FastAPI(title="Prisma Test", version="1.0.0", docs_url="/api/docs", openapi_url="/api/openapi.json")

app.include_router(author.author_router, prefix="/authors", tags=["Authors"])
app.include_router(post.post_router, prefix="/posts", tags=["Posts"])

@app.get("/")
async def root():
    return {"message": "Hello World"}