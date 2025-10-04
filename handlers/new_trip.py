from pydantic import BaseModel

from db_models.Trip import Trip, TRIP_STATE_FIRST_SURVEY
from stores import MainStore

from lib import db

class Model(BaseModel):
    token: str
    name: str
    description: str

def handle(event: Model, store: MainStore):
    print("Create trip!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    newTrip = Trip(user_id=userId, name=event.name, description=event.description, state=TRIP_STATE_FIRST_SURVEY,
                   orientality=0, temperature=0, historicity=0, sportiness=0, forest_cover=0, build_up_area=0,
                   terrain_fluctuation=0, water=0)
    db.session.add(newTrip)
    db.session.commit()

    return {"id": newTrip.id}

