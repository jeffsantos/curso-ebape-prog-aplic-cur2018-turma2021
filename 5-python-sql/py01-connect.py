import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Strings de conexão:
# Formato: 
# nome-servidor-bd://usuario:senha@endereco.do.servidor/nome-do-banco-de-dados
#
# Exemplos:
# sqlite:///flightsdb.sqlite3
# postgresql://postgres:aulasql@localhost/flightsdb
#
# Configure a variavel de ambiente DATABASE_URL no terminal para rodar o programa
# Exemplo:
# export DATABASE_URL=postgresql://postgres:aulasql@localhost/flightsdb

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT ori.name origin, dest.name destination, duration, flights.id  \
                        FROM flights \
                        JOIN locations ori on ori.id = flights.origin_id \
                        JOIN locations dest on dest.id = flights.destination_id").fetchall()
    for flight in flights:
        print(f"De {flight.origin} para {flight.destination} leva {flight.duration} minutos - {flight.id}")

if __name__ == "__main__":
    main()