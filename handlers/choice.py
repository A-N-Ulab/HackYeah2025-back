import traceback

from pydantic import BaseModel
from sqlalchemy.exc import NoReferencedTableError

from db_models.SurveyChoices import SurveyChoices
from db_models.Trip import Trip, TRIP_STATE_FIRST_SURVEY
from stores import MainStore

from lib import db

CHOICES_IN_BATCH = 15


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

    try:
        newChoice = SurveyChoices(trip_id=event.trip_id, destination_id=event.destination_id, choice=event.choice)
        db.session.add(newChoice)
        db.session.commit()
    except NoReferencedTableError as err:
        traceback.print_exc()
        return {"error": "Invalid ID", "detail": str(err)}, 404

    choicesCount = SurveyChoices.query.filter_by(trip_id=event.trip_id).count()

    return {"choice_idx": choicesCount, "total_choices": CHOICES_IN_BATCH}
