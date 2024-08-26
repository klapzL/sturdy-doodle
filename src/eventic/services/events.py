from src.common.service import BaseService
from src.eventic.models.events import Event


class EventsuctService(BaseService):
    model = Event
