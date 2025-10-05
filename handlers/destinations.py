import numpy as np
from pydantic import BaseModel
from sqlalchemy import select, literal, exists

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

    # (1) Wyrażenie na odległość^2 do bieżącego tripa
    dist2 = (
            (Destination.orientality - literal(trip.orientality)) ** 2 +
            (Destination.temperature - literal(trip.temperature)) ** 2 +
            (Destination.historicity - literal(trip.historicity)) ** 2 +
            (Destination.sportiness - literal(trip.sportiness)) ** 2 +
            (Destination.forest_cover - literal(trip.forest_cover)) ** 2 +
            (Destination.build_up_area - literal(trip.build_up_area)) ** 2 +
            (Destination.terrain_fluctuation - literal(trip.terrain_fluctuation)) ** 2 +
            (Destination.water - literal(trip.water)) ** 2
    ).label("dist2")

    # (2) Wyklucz destynacje już widziane/wybrane w tym tripie
    seen_exists = exists(
        select(1).where(
            (DestinationChoices.trip_id == event.trip_id) &
            (DestinationChoices.destination_id == Destination.id)
        )
    )

    # (3) (opcjonalnie) nie proponuj tej, którą właśnie przeglądano
    exclude_current = True
    where_clause = ~seen_exists
    if hasattr(event, "destination_id") and event.destination_id is not None:
        exclude_current = Destination.id != event.destination_id
        where_clause = where_clause & exclude_current

    # (4) Pobierz najbliższą
    row = db.session.execute(
        select(
            Destination.id,
            Destination.name,
            Destination.description,
            Destination.photo_name
        )
        .where(where_clause)
        .order_by(dist2.asc())
        .limit(1)
    ).first()

    return row
    # # (5) Zbuduj listę 'destinations' oczekiwaną przez Twój handler
    # destinations = []
    # if row:
    #     destinations.append({
    #         "id": row.id,
    #         "name": row.name,
    #         "description": row.description,
    #         "photo_name": row.photo_name,
    #     })
    # else:
    #     # Jeśli wszystko zostało już wykorzystane – możesz zwrócić pustą listę
    #     # lub np. błąd/komunikat o braku wyników.
    #     destinations = []
