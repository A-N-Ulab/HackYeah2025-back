from pydantic import BaseModel

from db_models.User import User
from lib import db
from stores.MainStore import MainStore


class Model(BaseModel):
    username: str
    password: str


def handle(event: Model, store: MainStore):
    print("Login!! ", event.model_dump())

    result = User.query.filter(User.username==event.username, User.password==event.password).first()

    if result is None:
        return {"Error": "Invalid username or password"}, 403

    userId = result.id

    token = store.tokens.getUserToken(userId)

    if token is None:
        # User not yet logged in - create new token
        token = store.tokens.createToken(userId)

    return {"token": token, "user_id": userId}
