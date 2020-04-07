#!/usr/bin/env python

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///devcor_test.db')
connection = engine.connect()

Base = declarative_base()

#define our tables
class customer(Base):
    __tablename__ = 'customers'
    Id = db.Column(db.Integer(), primary_key=True, unique=True)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    ZipCode = db.Column(db.Integer())

class order(Base):
    __tablename__ = 'orders'
    Id = db.Column(db.Integer(), primary_key=True, unique=True)
    Date = db.Column(db.String())
    Amount = db.Column(db.Float())
    CustomerId = db.Column(db.Integer, db.ForeignKey('customers.Id'))


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
my_session = session()
new_c = customer(FirstName="Bob", LastName="Dylan", Email="bob@dylan.com", ZipCode=55417)

my_session.add(new_c)

my_session.commit()
my_session.query(customer).all()

for each_c in my_session.query(customer).all():
    print(each_c.FirstName, each_c.LastName)

dylan_id = my_session.query(customer).filter_by(LastName='Dylan').all()
for records in dylan_id:
    fk = records.Id
new_order = order(Date="2020-04-07", Amount="56.08", CustomerId=fk)
my_session.add(new_order)
my_session.commit()
for each_order in my_session.query(order).all():
    print(each_order.Amount, each_order.CustomerId)






