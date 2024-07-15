from db.data.people import p1,p2,p3
from db.data.thing import t1,t2,t3,t4,t5
from models.person_model import Person
from models.thing_model import Thing

Person.insert_person(p1)
Person.insert_person(p2)
Person.insert_person(p3)

Thing.insert_thing(t1)
Thing.insert_thing(t2)
Thing.insert_thing(t3)
Thing.insert_thing(t4)
Thing.insert_thing(t5)
