from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
        
    return render_template("index.html", notes=notes)

