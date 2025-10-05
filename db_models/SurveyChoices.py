from lib import db


class SurveyChoices(db.Model):
    __tablename__ = 'survey_choices'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer)
    destination_id = db.Column(db.Integer)
    choice = db.Column(db.Boolean, nullable=False)
