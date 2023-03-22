from flask import Flask, render_template
from logger import log

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return "Hello World"
