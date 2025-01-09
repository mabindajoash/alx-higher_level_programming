#!/usr/bin/python3


from sqlalchemy import create_engine, Column, Integer, Table, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

metadata = MetaData()
Base = declarative_base(metadata)
class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
