from prisma import Prisma

async def db_session():
    db = Prisma()
    await db.connect()
    try:
        yield db
    finally:
        await db.disconnect()