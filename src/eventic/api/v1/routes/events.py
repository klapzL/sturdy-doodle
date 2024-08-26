from typing import List

from fastapi import APIRouter

from src.config.database.session import DBSession
from src.eventic.schemas.events import (
    EventCreate,
    EventQuerySchema,
    EventSchema,
)
from src.eventic.services.events import EventService

router = APIRouter(prefix='/events', tags=['events'])


@router.get('/', response_model=List[EventSchema])
async def get_events(db: DBSession):
    return await EventService.get_all(db)


@router.get('/{event_id}', response_model=EventQuerySchema)
async def get_event(db: DBSession, event_id: int):
    return await EventService.get_obj(db, id=event_id)


@router.post('/')
async def create_event(db: DBSession, event: EventCreate):
    await EventService.create(db, **event.model_dump())

    return {'message': 'created!'}


@router.put('/{event_id}')
async def update_evente(db: DBSession, event_id: int, event: EventCreate):
    await EventService.update(db, {'id': event_id}, event.model_dump())

    return {'message': 'updated'}


@router.delete('/{event_id}')
async def remove_event(db: DBSession, event_id: int):
    await EventService.delete(db, id=event_id)

    return {'message': 'deleted'}
