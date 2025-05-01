import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs

load_dotenv()
engine = create_async_engine(url=os.getenv("DATABASE_URL"))
async_session = async_sessionmaker(bind=engine)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)