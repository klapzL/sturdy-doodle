from pydantic import BaseModel, ConfigDict

from src.eventic.enums.events import EventType


class EventsSchema(BaseModel):
    id: int

    name: str
    price: float
    type: EventType

    model_config = ConfigDict(from_attributes=True)


class EventsQuerySchema(BaseModel):
    name: str | None = None
    price: float | None = None
    type: EventType | None = None


class EventsCreate(BaseModel):
    name: str
    price: float
    type: EventType
