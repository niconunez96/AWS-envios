import json
from botocore.exceptions import ClientError
from utils.response import success_response, not_found_response
from utils.dynamo_db import get_dynamodb_client, SHIPMENT_TABLE


def handler(event: dict, context: object) -> dict:
    dynamodb = get_dynamodb_client("dynamodb")
    table = dynamodb.Table(SHIPMENT_TABLE)

    parameters = event.get("pathParameters")
    id = str(parameters.get("idEnvio"))

    try:
        item = table.get_item(Key={"id": id})["Item"]
    except (ClientError, KeyError):
        return not_found_response(
            json.dumps({"message": "Shipment does not exist"})
        )

    table.delete_item(Key={"id": id})

    item.pop("pending")
    table.put_item(Item=item)

    return success_response(json.dumps(item))
