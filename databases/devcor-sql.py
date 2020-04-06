#!/usr/bin/env python

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///devcor_test.db')
connection = engine.connect()

Base = declarative_base()

#define our tables
class albums(Base):
    __tablename__ = 'albums'
    Id = db.Column(db.Integer(), primary_key=True, unique=True)
    Title = db.Column(db.String(255))

class artists(Base):
    __tablename__ = 'artists'
    Id = db.Column(db.Integer(), primary_key=True, unique=True)
    artist = db.Column(db.String(255))


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
my_session = session()
new_artist = artists(artist="Bob Dylan")

my_session.add(new_artist)

my_session.commit()
my_session.query(artists).all()

for each_artist in my_session.query(artists).all():
    print(each_artist.artist)



