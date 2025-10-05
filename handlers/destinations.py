import numpy as np
from pydantic import BaseModel

from Constants import CHOICES_IN_BATCH
from db_models.Destination import Destination
from db_models.Trip import Trip
from lib import db
from stores import MainStore


class Model(BaseModel):
    token: str
    trip_id: int


def handle(event: Model, store: MainStore):
    trip = Trip.query.filter_by(id=event.trip_id).first()

    if trip is None:
        return {"error": "Trip not found"}, 404

    destinations = []

    allIds = [int(r[0]) for r in db.session.query(Destination.id).all()]

    choices = np.random.choice(allIds, size=CHOICES_IN_BATCH, replace=False).tolist()

    allResults = Destination.query.filter(Destination.id.in_(choices)).all()

    if len(allResults) == 0:
        return {"error": "Internal server error"}, 500

    for result in allResults:
        destinations.append({
            "id": result.id,
            "name": result.name,
            "description": result.description,
            "photo_name": result.photo_name,
        })

    response = {"destinations": destinations, "state": trip.state}

    return response
