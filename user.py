# coding: UTF-8

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE

#class クラス名(Base)
class User(Base):
    
    #テーブル名を定義
    __tablename__ = 'users'

    #カラムを定義
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    password = Column('password',String(20))

#うーん、
def main(args):
    Base.metadata.create_all(bind=ENGINE)

#おまじない
if __name__ == "__main__":
    main(sys.argv)