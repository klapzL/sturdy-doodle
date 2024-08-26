from pydantic import BaseModel, ConfigDict

from src.eventic.enums.events import EventType


class EventSchema(BaseModel):
    id: int

    name: str
    type: EventType

    model_config = ConfigDict(from_attributes=True)


class EventQuerySchema(BaseModel):
    name: str | None = None
    type: EventType | None = None


class EventCreate(BaseModel):
    name: str
    type: EventType
