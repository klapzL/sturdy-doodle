from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from src.common.exceptions import BadRequestException, NotFoundException
from src.common.models import BaseModel
from src.config.database.session import DBSession

T = TypeVar('T', bound=BaseModel)


class BaseService(Generic[T]):
    model: Type[T]

    @classmethod
    async def _fetch_records(cls, db: DBSession, **data):
        q = select(cls.model).filter_by(**data)
        result = await db.execute(q)
        return result.scalars()

    @classmethod
    async def get(cls, db: DBSession, filter_data):
        objs = await cls._fetch_records(db)

        return objs.one()

    @classmethod
    async def get_all(cls, db: DBSession, **data):
        objs = await cls._fetch_records(db, **data)

        return objs.all()

    async def get_paginated(cls, db: DBSession, **data):
        objs = await cls.get(db, **data)
        return objs

    @classmethod
    async def get_obj(cls, db: DBSession, **data) -> T:
        record = await cls._fetch_records(db, **data)

        try:
            obj = record.one()
            pass
        except NoResultFound:
            raise NotFoundException
        except MultipleResultsFound:
            raise BadRequestException('Multiple results found.')

        return obj

    @classmethod
    async def create(cls, db: DBSession, **data):
        obj = cls.model(**data)

        db.add(obj)
        await db.commit()

    @classmethod
    async def update(cls, db: DBSession, data: dict, new_data: dict):
        obj = await cls.get(db, **data)
        await obj.update(**new_data)

        await db.commit()

    @classmethod
    async def delete(cls, db: DBSession, **data):
        obj = cls.get_obj(db, **data)

        await db.delete(obj)
        await db.commit()
