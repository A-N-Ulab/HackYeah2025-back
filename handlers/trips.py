from pydantic import BaseModel

from db_models.Trip import Trip
from stores import MainStore

from lib import db

class Model(BaseModel):
    token: str

def handle(event: Model, store: MainStore):
    print("Get trips!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    trips = Trip.query.filter_by(user_id=userId).all()
    print(len(trips))

    trip_list = [
        {
            "id": trip.id,
            "name": trip.name,
            "description": trip.description,
        }
        for trip in trips
    ]



    return {"trips": trip_list}
