import json
from utils.response import success_response
from utils.dynamo_db import (
    get_dynamodb_client,
    PENDING_SHIPMENTS_INDEX,
    SHIPMENT_TABLE,
)


def handler(event: dict, context: object) -> dict:
    dynamodb = get_dynamodb_client("dynamodb")
    table = dynamodb.Table(SHIPMENT_TABLE)
    response = table.scan(
        IndexName=PENDING_SHIPMENTS_INDEX,
    )
    items = json.dumps(response["Items"])
    return success_response(items)
