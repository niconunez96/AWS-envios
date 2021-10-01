def success_response(message: str) -> dict:
    return {
        "statusCode": 200,
        "body": message,
    }


def not_found_response(message: str) -> dict:
    return {
        "statusCode": 404,
        "body": message,
    }
