import numpy as np
from pydantic import BaseModel
from sqlalchemy import select, exists, literal
from sqlalchemy.sql import and_, not_
from sqlalchemy import func  # opcjonalnie, gdybyś chciał użyć func.power

from Constants import CHOICES_IN_BATCH
from db_models.Destination import Destination
from db_models.DestinationChoices import DestinationChoices
from db_models.Trip import Trip, TRIP_STATE_SWAPPING, TRIP_STATE_FIRST_SURVEY
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
    if trip.state == TRIP_STATE_FIRST_SURVEY:
        destinations = []

        allIds = [int(r[0]) for r in db.session.query(Destination.id).all()]
        batch_choices = DestinationChoices.query.filter_by(trip_id=event.trip_id).all()

        choices = np.random.choice(allIds, size=CHOICES_IN_BATCH-len(batch_choices), replace=False).tolist()

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



    destinations = []
    response_destination = generate_algorithm_outcome(event, trip)

    destinations.append({
        "id": response_destination.id,
        "name": response_destination.name,
        "description": response_destination.description,
        "photo_name": response_destination.photo_name,
    })

    response = {"destinations": destinations, "state": trip.state}

    return response


def generate_algorithm_outcome(event: Model, trip: Trip):
    # różnice cech do aktualnego tripa
    diffs = [
        (Destination.orientality - literal(trip.orientality)),
        (Destination.temperature - literal(trip.temperature)),
        (Destination.historicity - literal(trip.historicity)),
        (Destination.sportiness - literal(trip.sportiness)),
        (Destination.forest_cover - literal(trip.forest_cover)),
        (Destination.build_up_area - literal(trip.build_up_area)),
        (Destination.terrain_fluctuation - literal(trip.terrain_fluctuation)),
        (Destination.water - literal(trip.water)),
    ]

    # suma kwadratów (bez ** — używamy mnożenia)
    # równoważne: sum(func.power(d, 2) for d in diffs)
    dist2 = sum(d * d for d in diffs).label("dist2")

    # wyklucz już występujące w DestinationChoices dla tego tripa
    seen = exists(
        select(1).where(
            (DestinationChoices.trip_id == trip.id) &
            (DestinationChoices.destination_id == Destination.id)
        )
    )

    stmt = (
        select(
            Destination.id,
            Destination.name,
            Destination.description,
            Destination.photo_name,
            dist2,
        )
        .where(not_(seen))
    )

    # (opcjonalnie) nie proponuj tej samej, którą właśnie przeglądano
    if getattr(event, "destination_id", None) is not None:
        stmt = stmt.where(Destination.id != event.destination_id)

    # najbliższa po dist2
    stmt = stmt.order_by(dist2.asc()).limit(1)

    row = db.session.execute(stmt).first()
    return row
