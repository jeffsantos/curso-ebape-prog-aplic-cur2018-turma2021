import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Antes de executar o código, configure a variável DATABASE_URL 
# no seu terminal com o comando: 
# export DATABASE_URL=postgresql://postgres:sua-senha@localhost/nome-do-banco
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main(): 
    flights = db.execute("SELECT * FROM flights").fetchall()

    for flight in flights:
        print(f"Vôo de {flight.origin_id} para {flight.destination_id} leva {flight.duration}")

if __name__ == "__main__":
    main()