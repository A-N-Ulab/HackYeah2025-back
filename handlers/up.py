from pydantic import BaseModel

from db_models.SavedPhotos import SavedPhotos
from stores import MainStore

from lib import db

class Model(BaseModel):
    token: str
    photo_id: int

def handle(event: Model, store: MainStore):
    print("Save photo!! ", event.model_dump())

    userId = store.tokens.getUserId(event.token)

    if userId is None:
        return {"error": "Invalid token"}, 403

    saved_photo = SavedPhotos(user_id=userId, destination_id=event.photo_id)
    db.session.add(saved_photo)
    db.session.commit()


    return {"status": "saved"}
