from typing import List

from fastapi import APIRouter

from src.config.database.session import DBSession
from src.eventic.schemas.events import (
    EventsuctCreate,
    EventsuctQuerySchema,
    EventsuctSchema,
)
from src.eventic.services.events import EventsuctService

router = APIRouter(prefix='/events', tags=['events'])


@router.get('/', response_model=List[EventsuctSchema])
async def get_Eventsucts(db: DBSession):
    return await EventsuctService.get(db)


@router.get('/{Eventsuct_id}', response_model=EventsuctQuerySchema)
async def get_Eventsuct(db: DBSession, Eventsuct_id: int):
    return await EventsuctService.get_obj(db, id=Eventsuct_id)


@router.post('/')
async def create_Eventsuct(db: DBSession, event: EventsuctCreate):
    await EventsuctService.create(db, **event.model_dump())

    return {'message': 'created!'}


@router.put('/{Eventsuct_id}')
async def update_Eventsuct(db: DBSession, Eventsuct_id: int, event: EventsuctCreate):
    await EventsuctService.update(db, {'id': Eventsuct_id}, event.model_dump())

    return {'message': 'updated'}


@router.delete('/{Eventsuct_id}')
async def remove_Eventsuct(db: DBSession, Eventsuct_id: int):
    await EventsuctService.delete(db, id=Eventsuct_id)

    return {'message': 'deleted'}
