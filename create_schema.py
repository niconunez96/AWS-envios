from boto3.dynamodb.types import STRING

from endpoints.utils.dynamo_db import get_dynamodb_client


def create_table():
    dynamodb = get_dynamodb_client()

    table = dynamodb.create_table(
        TableName="Shipment",
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},  # Partition key
        ],
        GlobalSecondaryIndexes=[
            {
                "IndexName": "PendingShipmentsIndex",
                "KeySchema": [
                    {"AttributeName": "id", "KeyType": "HASH"},
                    {"AttributeName": "pending", "KeyType": "RANGE"},
                ],
                "Projection": {"ProjectionType": "ALL"},
                "ProvisionedThroughput": {
                    "WriteCapacityUnits": 1,
                    "ReadCapacityUnits": 1,
                },
            }
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": STRING},
            {"AttributeName": "pending", "AttributeType": STRING}
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    return table


if __name__ == "__main__":
    movie_table = create_table()
    print(f"Table status: {movie_table.table_status}")
