from lib import db


class SavedPhotos(db.Model):
    __tablename__ = "saved_photos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    destination_id = db.Column(db.Integer, nullable=False)