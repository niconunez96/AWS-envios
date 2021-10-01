from decimal import Decimal
from endpoints.utils.dynamo_db import get_dynamodb_client
import json


def load_movies(movies):
    dynamodb = get_dynamodb_client()

    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)


if __name__ == '__main__':
    with open("data.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)
