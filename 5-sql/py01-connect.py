import os

from sqlalchemy import create_engine
from sqlalchemy import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main(): 
    flights = db.execute("SELECT * FROM flights").fetchall()

    for flight in flights:
        print(f"Vôo de {flight.origin_id} para {flight.destination_id} leva {flight.duration}")

if __name__ == "__main__":
    main()