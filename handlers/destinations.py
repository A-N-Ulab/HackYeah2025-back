from pydantic import BaseModel

from db_models.Destination import Destination
from db_models.Trip import Trip
from stores import MainStore


class Model(BaseModel):
    token: str
    trip_id: int


def handle(event: Model, store: MainStore):
    count = 1
    print(f"Generating next '{count}' destination")

    trip = Trip.query.filter_by(id=event.trip_id).first()

    if trip is None:
        return {"error": "Trip not found"}, 404

    destinations = []

    result = Destination.query.filter_by(id=1).first()

    if result is None:
        return {"error": "Internal server error"}, 500

    destinations.append({
        "id": result.id,
        "name": result.name,
        "description": result.description,
        "photo_name": result.photo_name,
    })

    response = {"destinations": destinations, "state": trip.state}
    return response
