from src.common.service import BaseService
from src.eventic.models.events import Event


class EventsService(BaseService):
    model = Event
