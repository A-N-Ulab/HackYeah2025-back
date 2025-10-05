from pydantic import BaseModel

from db_models.SavedPhotos import SavedPhotos
from db_models.Destination import Destination
from stores import MainStore

from lib import db

class Model(BaseModel):
    token: str

def handle(event: Model, store: MainStore):
    print("Get photos!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    photos_all = SavedPhotos.query.filter_by(user_id=userId).all()
    print(len(photos_all))
    photos_list = []

    for photo in photos_all:
        destination = Destination.query.filter_by(id=photo.id).first()
        photos_list.append({
            "id": photo.id,
            "name": destination.name,
            "description": destination.description,
            "photo_name": destination.photo_name
        })




    return {"status": "saved"}
