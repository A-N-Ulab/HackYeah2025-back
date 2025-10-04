import importlib
import os
import traceback
from typing import Union

from dotenv import load_dotenv
from flask import Flask
from flask import request
from flask_cors import CORS
from pydantic import BaseModel, ValidationError

from db_models.User import User
from lib import db
from stores.MainStore import MainStore


def create_app():
    app = Flask(__name__)

    load_dotenv()

    CORS(app, supports_credentials=True, origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://hy25.anulab.tech",
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

    global main_store
    main_store = MainStore()

    return app


main_store: MainStore  # set in create_app
app = create_app()


@app.route("/")
def hello_world():
    return {"hi": "me"}


@app.route('/<path:path>', methods=['POST'])
def general_endpoint_handler(path: str) -> Union[dict, tuple[dict, int]]:
    handlerName = path

    bodyDict = request.json

    if os.path.isfile(f"handlers/{handlerName}.py"):
        handlerModule = importlib.import_module(
            f"handlers.{handlerName}"
        )
    else:
        return {"error": f"Invalid endpoint: '{path}'"}, 404

    assert hasattr(handlerModule, "handle"), "Handler not set up properly: No 'handle' method"
    assert hasattr(handlerModule, "Model"), "Handler not set up properly: No 'Model' class"

    handleMethod = getattr(handlerModule, "handle")
    ReqModel = getattr(handlerModule, "Model")

    assert callable(handleMethod), "Handler not set up properly: 'handle' method should be callable"
    assert issubclass(ReqModel, BaseModel), "Handler not set up properly: 'Model' class should inherit from BaseModel"

    try:
        reqBody = ReqModel(**bodyDict)
    except ValidationError as err:
        errors = err.errors(include_input=False)
        return {"error": errors}, 400

    try:
        resp = handleMethod(reqBody, main_store)
        return resp
    except Exception:
        traceback.print_exc()
        return {"error": "Internal server error"}, 500


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
        "users": [],
        "foo": "Bar",
    }

    for result in results:
        response["users"].append({"id": result.id, "username": result.username})

    return response

