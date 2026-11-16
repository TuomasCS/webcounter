from flask import Flask, abort, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set-clicks", methods=["POST"])
def set_clicks():
    value = request.form.get("clicks", type=int)
    if value is None or value < 0:
        abort(400)
    cnt.set_value(value)
    return redirect("/")
