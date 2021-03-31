import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    agora = datetime.datetime.now()

    is_it_easter = (agora.month == 4 and agora.day == 4 and agora.year == 2021)

    return render_template("index.html", is_it_easter=is_it_easter)