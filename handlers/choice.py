from pydantic import BaseModel

from db_models.Trip import Trip, TRIP_STATE_FIRST_SURVEY
from stores import MainStore

from lib import db


class Model(BaseModel):
    token: str
    trip_id: int
    destination_id: int
    choice: bool


def handle(event: Model, store: MainStore):
    print("You choice sth.!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    trip = Trip.query.filter_by(user_id=userId, id=event.trip_id).first()

    if trip is None:
        return {"error": "Trip not found"}, 404


    return {}
