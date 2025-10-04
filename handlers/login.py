from pydantic import BaseModel

from db_models.User import User
from lib import db
from stores.MainStore import MainStore


class Model(BaseModel):
    username: str
    password: str


def handle(event: Model, store: MainStore):
    print("Login!! ", event.model_dump())

    query = db.session.query(User).filter(User.username==event.username, User.password==event.password)
    result = query.one_or_none()

    if result is None:
        return {"Error": "Invalid username or password"}, 403

    userId = result.id

    token = store.tokens.createToken(userId)

    return {"token": token, "user_id": userId}
