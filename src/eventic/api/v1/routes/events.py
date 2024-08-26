from typing import List

from fastapi import APIRouter

from src.config.database.session import DBSession
from src.eventic.schemas.events import (
    EventsCreate,
    EventsQuerySchema,
    EventsSchema,
)
from src.eventic.services.events import EventsService

router = APIRouter(prefix='/events', tags=['events'])


@router.get('/', response_model=List[EventsSchema])
async def get_Eventss(db: DBSession):
    return await EventsService.get(db)


@router.get('/{Events_id}', response_model=EventsQuerySchema)
async def get_Events(db: DBSession, Events_id: int):
    return await EventsService.get_obj(db, id=Events_id)


@router.post('/')
async def create_Events(db: DBSession, event: EventsCreate):
    await EventsService.create(db, **event.model_dump())

    return {'message': 'created!'}


@router.put('/{Events_id}')
async def update_Events(db: DBSession, Events_id: int, event: EventsCreate):
    await EventsService.update(db, {'id': Events_id}, event.model_dump())

    return {'message': 'updated'}


@router.delete('/{Events_id}')
async def remove_Events(db: DBSession, Events_id: int):
    await EventsService.delete(db, id=Events_id)

    return {'message': 'deleted'}
