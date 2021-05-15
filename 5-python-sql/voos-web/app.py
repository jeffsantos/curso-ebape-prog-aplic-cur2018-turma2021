import os

from flask import Flask, render_template, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT ori.name origin, dest.name destination, duration, flights.id  \
                        FROM flights \
                        JOIN locations ori on ori.id = flights.origin_id \
                        JOIN locations dest on dest.id = flights.destination_id").fetchall()

    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    passageiro = request.form.get("name")

    if passageiro == "":
        return render_template("error.html", message="Passageiro precisa ser informado!!")

    try:
        voo = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("erro.html", message="Voo inválido!!")

    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
                {"name":passageiro, "flight_id":voo})
    db.commit()
 
    return render_template("success.html")
