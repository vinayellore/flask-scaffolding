import datetime

from sqlalchemy.ext.declarative import declared_attr

from extensions import db


class Base(db.Model):
    """This is Base model which common to all models. Its a abstract class"""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, default=datetime.datetime.utcnow(),
                           onupdate=datetime.datetime.utcnow())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return str(self.as_dict())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
