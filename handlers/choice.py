import traceback

from pydantic import BaseModel
from sqlalchemy.exc import NoReferencedTableError

from Constants import CHOICES_IN_BATCH
from algorithm.alogrithm import create_first_time

from db_models.Destination import Destination
from db_models.DestinationChoices import DestinationChoices
from db_models.Trip import Trip, TRIP_STATE_SWAPPING, TRIP_STATE_FIRST_SURVEY

from stores import MainStore

from lib import db


class Model(BaseModel):
    token: str
    trip_id: int
    destination_id: int
    choice: bool


def handle(event: Model, store: MainStore):
    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    trip = Trip.query.filter_by(user_id=userId, id=event.trip_id).first()

    if trip is None:
        return {"error": "Trip not found"}, 404
    if trip.state == TRIP_STATE_FIRST_SURVEY:
        try:
            newChoice = DestinationChoices(trip_id=event.trip_id, destination_id=event.destination_id, choice=event.choice)
            db.session.add(newChoice)
            db.session.commit()
        except NoReferencedTableError as err:
            traceback.print_exc()
            return {"error": "Invalid ID", "detail": str(err)}, 404

        batch_choices = DestinationChoices.query.filter_by(trip_id=event.trip_id).all()

        if len(batch_choices) >= CHOICES_IN_BATCH:
            # prepare for algorithm
            features_vectors: list[list[float]] = []
            choices: list[bool] = []
            for batch_choice in batch_choices:
                destination  = Destination.query.filter_by(id=batch_choice.destination_id).first()

                features_vectors.append([destination.orientality, destination.temperature, destination.historicity,
                                         destination.sportiness, destination.forest_cover, destination.build_up_area,
                                         destination.terrain_fluctuation, destination.water])
                choices.append(batch_choice.choice)

            algo_solution = create_first_time(features_vectors, choices)

            # add to trips
            for solution in algo_solution.keys():
                setattr(trip, solution, algo_solution[solution])
            setattr(trip, "state", TRIP_STATE_SWAPPING)

            db.session.commit()
        # inside first surway if
        return {"choice_idx": len(batch_choices), "total_choices": CHOICES_IN_BATCH}

    # infinite loop of swapping until ... ! bool value
    return {"survey":"ok"}
