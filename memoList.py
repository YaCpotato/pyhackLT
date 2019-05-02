# coding: UTF-8

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from setting import Base
from setting import ENGINE

class MemoList(Base):
    __tablename__ = 'memoList'
    id = Column('id', Integer, primary_key = True)
    category = Column('category', String(200))
    main = Column('main',String(200))
    link = Column('link',String(200))

ma = Marshmallow()
class MemoListSchema(ma.ModelSchema):
    class Meta:
        model = MemoList


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)