from lib import db


class SurveyChoices(db.Model):
    __tablename__ = 'survey_choices'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    choice = db.Column(db.Boolean, nullable=False)
