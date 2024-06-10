from fastapi_pagination.ext.sqlalchemy import paginate

from src.common.models import BaseModel
from src.config.database import DBSession


class BaseService():
    model: BaseModel

    @classmethod
    def filter(cls, db: DBSession, **data):
        return db.query(cls.model).filter_by(**data)

    @classmethod
    def get(cls, db: DBSession, **data):
        return paginate(cls.filter(db, **data).all())

    @classmethod
    def get_obj(cls, db: DBSession, **data):
        return cls.filter(db, **data).first()

    @classmethod
    def create(cls, db: DBSession, **data):
        obj = cls.model(**data)

        db.add(obj)
        db.commit()

    @classmethod
    def update(cls, db: DBSession, **data):
        cls.filter(db, **data).update(data)
        db.commit()

    @classmethod
    def delete(cls, db: DBSession, **data):
        cls.filter(db, **data).delete()
        db.commit()
