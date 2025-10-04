from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"hi": "me"}


@app.route("/test")
def test_endpoint():
    return {"test": "endpoint"}

