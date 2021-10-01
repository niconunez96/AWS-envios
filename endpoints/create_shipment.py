from datetime import datetime
import json
import uuid
from utils.response import success_response
from utils.dynamo_db import get_dynamodb_client, SHIPMENT_TABLE


def handler(event: dict, context: object) -> dict:
    body = event["body"]
    print(body)
    dynamodb = get_dynamodb_client("dynamodb")
    table = dynamodb.Table(SHIPMENT_TABLE)

    new_id = uuid.uuid4()
    item = {
        "id": str(new_id),
        "pending": str(datetime.now()),
        **json.loads(body)
    }
    print(item)
    table.put_item(Item=item)
    return success_response(json.dumps({'id': str(new_id)}))
