from pydantic import BaseModel

from db_models.Trip import Trip, TRIP_STATE_FIRST_SURVEY
from stores import MainStore

from lib import db

class Model(BaseModel):
    token: str
    id: int

def handle(event: Model, store: MainStore):
    print("Delete trip!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    Trip.query.filter_by(user_id=userId, id=event.id).delete()
    db.session.commit()

    return {}