from sqlalchemy import DateTime

from lib import db


class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.String(40), primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(DateTime)
    expires_at = db.Column(DateTime)
