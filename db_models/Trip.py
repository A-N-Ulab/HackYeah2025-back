from lib import db

TRIP_STATE_FIRST_SURVEY = "first_survey"
TRIP_STATE_SWAPPING = "swapping"


class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    state = db.Column(db.String, nullable=False)
    """
    Available values:
    
    - "first_survey" - establishing base preferences based on batch of photos
    - "swapping" - fine tuning preferences on each swap
    """

    orientality = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    historicity = db.Column(db.Float, nullable=False)
    sportiness = db.Column(db.Float, nullable=False)
    forest_cover = db.Column(db.Float, nullable=False)
    build_up_area = db.Column(db.Float, nullable=False)
    terrain_fluctuation = db.Column(db.Float, nullable=False)
    water = db.Column(db.Float, nullable=False)
