from sqlalchemy import Column, DateTime, func

from src.config.database import Base


class BaseModel(Base):
    __abstract__ = True

    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())
