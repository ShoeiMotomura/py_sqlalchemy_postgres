from sqlalchemy import ForeignKey, Column, String, Integer
from utils import Base, session
from models.person_model import Person

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"

    @classmethod
    def select_by_owner_firstname(cls, firstname):
        return session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == firstname).all()

    @classmethod
    def insert_thing(cls,t):
        session.add(t)
        session.commit()
