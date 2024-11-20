#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
It takes three arguments: mysql username, mysql password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server running on localhost
    # at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and join with State objects, sorted by cities.id
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
