from typing import List
from endpoints.utils.dynamo_db import get_dynamodb_client, SHIPMENT_TABLE
import json


def load_movies(shipments: List[dict]):
    dynamodb = get_dynamodb_client()

    table = dynamodb.Table(SHIPMENT_TABLE)
    for shipment in shipments:
        print("Adding shipment with id", shipment['id'])
        table.put_item(Item=shipment)


if __name__ == '__main__':
    with open("data.json") as json_file:
        shipments = json.load(json_file)
    load_movies(shipments)
