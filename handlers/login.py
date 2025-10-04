from pydantic import BaseModel


class Model(BaseModel):
    username: str
    password: str


def handle(event: Model) -> dict:
    print("Login!! ", event.model_dump())

    token = "fake_token"

    return {"token": token, "user_id": 13}
