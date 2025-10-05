from lib import db


class DestinationChoices(db.Model):
    __tablename__ = 'destination_choices'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer)
    destination_id = db.Column(db.Integer)
    choice = db.Column(db.Boolean, nullable=False)
