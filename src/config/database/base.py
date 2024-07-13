from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.settings import settings


async_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False, autocommit=False, autoflush=False, class_=AsyncSession)

Base = declarative_base()
