from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"hi": "me"}


@app.route("/test")
def test_endpoint():
    return {"test": "endpoint"}
