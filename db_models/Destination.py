from lib import db

class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    photo_name = db.Column(db.String, nullable=False)
    orientality = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    historicity = db.Column(db.Float, nullable=False)
    sportiness = db.Column(db.Float, nullable=False)
    forest_cover = db.Column(db.Float, nullable=False)
    build_up_area = db.Column(db.Float, nullable=False)
    terrain_fluctuation = db.Column(db.Float, nullable=False)
    water = db.Column(db.Float, nullable=False)
