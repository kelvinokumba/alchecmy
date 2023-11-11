from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

engine= create_engine('postgresql://jerinjose:jerinjose@localhost:5432/alchemy',echo=False)
session= sessionmaker(bind=engine)
session =session()

Base = declarative_base()

class Student(Base):
    __tablename__='student'

    id=Column(Integer, primary_key=True)
    name=Column(String (50))
    age=Column(Integer)
    grade=Column(Integer)

Base.metadata.create_engine(engine)

