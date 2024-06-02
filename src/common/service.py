from fastapi_pagination import paginate

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
    def delete(cls, db: DBSession, **data):
        db.query(cls.model).filter_by(**data).delete()
        db.commit()

    @classmethod
    def create(cls, db: DBSession, **data):
        obj = cls.model(**data)

        db.add(obj)
        db.commit()
