from sqlalchemy import Column, DateTime, Enum, Integer, String

from src.common.models import BaseModel
from src.eventic.enums.events import EventType


class Event(BaseModel):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    date = Column(DateTime)
    type = Column(Enum(EventType))
