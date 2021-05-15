# 1. Listar todos os voos (OK)

# 2. Escolher um voo (OK)

    # 2.1 Testar se é valido ou nao. (OK)


# 3. Listar todos os passageiros do voo. 

    # 3.1 Mensagem caso não tenha nenhum passageiro. 

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine("postgresql://postgres:aulasql@localhost/flightsdb")

db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT ori.name origin, dest.name destination, duration, flights.id  \
                        FROM flights \
                        JOIN locations ori on ori.id = flights.origin_id \
                        JOIN locations dest on dest.id = flights.destination_id").fetchall()
    for flight in flights:
        print(f"De {flight.origin} para {flight.destination} leva {flight.duration} minutos - {flight.id}")

    flight_id = int(input("\nEscolha um voo: "))

    flight = db.execute("SELECT * FROM flights WHERE id = :flight_id",
                        {"flight_id": flight_id}).fetchone()

    if flight is None:
        print("Voo invalido")
        return

    passengers = db.execute("SELECT * FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()

    for passenger in passengers:
        print(passenger.name)

    if len(passengers) == 0:
        print("\nNenhum passsageiro no voo")
    

if __name__ == "__main__":
    main()