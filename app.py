import os

from flask import Flask

from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    load_dotenv()
    print("Environ:")
    print(os.environ)

    return app


app = create_app()


@app.route("/")
def hello_world():
    return {"hi": "me"}


@app.route("/test")
def test_endpoint():
    print("username: ", os.getenv("DB_USERNAME"))
    return {"test": "endpoint"}

