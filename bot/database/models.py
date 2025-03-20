from sqlalchemy import BigInteger, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import String

from config_reader import config

engine_url = config.sqlalchemy_url.get_secret_value()

engine = create_async_engine(f"{engine_url}")

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase, AsyncAttrs):
    pass

class User(Base):
    __tablename__ = "example-database"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id = mapped_column(BigInteger, unique=True)

async def connect_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)