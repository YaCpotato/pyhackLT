# coding: UTF-8

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE

#class クラス名(Base)
class MemoList(Base):

    #テーブル名を定義
    __tablename__ = 'memoList'

    #カラムを定義
    id = Column('id', Integer, primary_key = True)
    category = Column('category', String(200))
    main = Column('main',String(200))
    link = Column('link',String(200))

#うーん、、
def main(args):
    Base.metadata.create_all(bind=ENGINE)

#おまじない
if __name__ == "__main__":
    main(sys.argv)