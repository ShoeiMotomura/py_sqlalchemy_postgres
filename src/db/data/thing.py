from models.thing_model import Thing
from db.data.people import p1,p2,p3

t1 = Thing(1, "Car", p1.ssn)
t2 = Thing(2, "Laptop", p1.ssn)
t3 = Thing(3, "Pen", p2.ssn)
t4 = Thing(4, "Tool", p3.ssn)
t5 = Thing(5, "Book", p3.ssn)
