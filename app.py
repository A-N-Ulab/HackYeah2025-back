import os

from flask import Flask

from db_models.Users import User
from lib import db
from flask_cors import CORS

from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    load_dotenv()
    print("Environ:")
    print(os.environ)

    CORS(app, supports_credentials=True, origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ])

    USER = os.getenv("DB_USERNAME")
    PASSWORD = os.getenv("DB_PASS")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DBNAME = os.getenv("DB_NAME")

    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app


app = create_app()


@app.route("/")
def hello_world():
    return {"hi": "me"}


@app.route("/test")
def test_endpoint():
    print("username: ", os.getenv("DB_USERNAME"))
    return {"test": "endpoint", "user": os.getenv("DB_USERNAME")}


@app.route("/users")
def get_users():
    print("DB test")

    results = User.query.all()

    print("query results: ", results)

    response = {
        "users": []
    }

    for result in results:
        response["users"].append({"id": result.id, "username": result.username})

    return response

