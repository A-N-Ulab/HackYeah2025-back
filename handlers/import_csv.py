import csv

from pydantic import BaseModel

from db_models.Destination import Destination
from lib import db
from stores.MainStore import MainStore


class Model(BaseModel):
    csv_path: str


def handle(event: Model, store: MainStore):
    return {"error": "temporarily unavailable"}, 404

    print("CSV Path: ", event.csv_path)

    with open(event.csv_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))

        data = reader[1:]

    for row in data:
        print(f"{row=}")

        dataRow = {
            "name": str(row[0]),
            "description": str(row[1]),
            "photo_name": str(row[2]),
            "orientality": float(row[3]),
            "temperature": float(row[4]),
            "historicity": float(row[5]),
            "sportiness": float(row[6]),
            "forest_cover": float(row[7]),
            "build_up_area": float(row[8]),
            "terrain_fluctuation": float(row[9]),
            "water": float(row[10]),
        }
        print(f"{dataRow=}")
        record = Destination(**dataRow)
        db.session.add(record)

    db.session.commit()

    return {}
