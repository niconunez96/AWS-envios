import boto3

SHIPMENT_TABLE = "Shipment"
PENDING_SHIPMENTS_INDEX = "PendingShipmentsIndex"


def get_dynamodb_client(host: str = "localhost"):
    return boto3.resource(
        "dynamodb",
        endpoint_url=f"http://{host}:8000",
        region_name="us-west-2",
        aws_access_key_id="2345",
        aws_secret_access_key="2345",
    )
