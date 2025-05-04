import logging
import os

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = os.environ.get("DATABASE_URL")

Base = declarative_base()

engine = create_async_engine(DB_URL, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

log = logging.getLogger("uvicorn")


async def init_db():
    """Verify database connection"""
    try:
        async with engine.begin() as conn:
            await conn.execute("SELECT 1")
    except Exception as e:
        log.error(f"Database is not running: {e}")
        raise


async def get_db() -> AsyncSession:
    """Yield a database session"""
    async with async_session() as session:
        yield session

class DB(AsyncSession):
    def __new__(cls,db: AsyncSession = Depends(get_db)):
        return db