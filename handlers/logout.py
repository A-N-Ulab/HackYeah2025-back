from pydantic import BaseModel

from stores.MainStore import MainStore


class Model(BaseModel):
    token: str


def handle(event: Model, store: MainStore):
    success = store.tokens.deleteToken(event.token)

    if success:
        return {}
    else:
        return {"error": "Invalid token"}, 403
