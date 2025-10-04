from pydantic import BaseModel


class Model(BaseModel):
    username: str
    password: str


def handle(event: Model) -> dict:
    print("Login!! ", event.model_dump())

    return {"your username: ": event.username}
