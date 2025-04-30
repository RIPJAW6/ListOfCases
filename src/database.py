from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(engine)
session = Session()

class Base(DeclarativeBase):
    metadata = MetaData()