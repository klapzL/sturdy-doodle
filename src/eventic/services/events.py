from src.common.service import BaseService
from src.eventic.models.events import Event


class EventService(BaseService):
    model = Event
