import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

from app.config import PostgresDB


DATABASE_URL = f"postgresql+asyncpg://{PostgresDB.USER}:{PostgresDB.PASSWORD}@{PostgresDB.HOST}:{PostgresDB.PORT}/{PostgresDB.NAME}"

engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    echo=True)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def test_connection():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ Connection successful:", result.scalar())
    except Exception as e:
        print("❌ Connection failed:", e)


def main() -> None:
    asyncio.run(test_connection())


if __name__ == "__main__":
    main()