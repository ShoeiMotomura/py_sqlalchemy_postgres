from sqlalchemy import Column, String, Integer, CHAR
from utils import Base, session

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column ("age" , Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"

    @classmethod
    def select_all(cls):
        return session.query(cls).all()

    @classmethod
    def select_by_lastname(cls, lastname):
        return session.query(cls).filter(cls.lastname == lastname)
    
    @classmethod
    def insert_person(cls, p):
        session.add(p)
        session.commit()
