# coding: UTF-8

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from setting import Base
from setting import ENGINE

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    password = Column('password',String(20))

ma = Marshmallow()
class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)