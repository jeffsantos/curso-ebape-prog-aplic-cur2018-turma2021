from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    subhead = "Outra forma de dar Hello!!"
    return render_template("index.html", subhead=subhead)