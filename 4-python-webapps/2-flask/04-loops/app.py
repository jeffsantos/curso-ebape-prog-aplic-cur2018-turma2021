import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Jefferson", "Gabriel", "Renata"]
    names.append("Carlos")
    return render_template("index.html", names=names)