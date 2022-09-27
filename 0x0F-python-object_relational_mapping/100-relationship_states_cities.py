#!/usr/bin/python3

from sys import argv
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="San Francisco")
    california.cities = [City(name="California")]
    session.add(california)
    session.commit()
    session.close()