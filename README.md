# Practico AWS DynamoDB y Lambda

## Setup
Requisitos:
1. Python3
2. AWS SAM
3. Docker 

## Instalar dependencias de python:
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r endpoints/requirements.txt`

## Setup
1. Crear una red con docker `docker network create awslocal` 
2. Levantar dynamodb con docker `docker run -p 8000:8000 --network awslocal --name dynamodb amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb`
3. Crear el schema de base de datos con `python create_schema.py`
    - Opcional: Para cargar unos datos de ejemplos se puede correr `python load_data.py`
4. Levantar lambdas con `sam local start-api --docker-network awslocal`

## Uso

La aplicacion tiene 3 endpoints

1. `GET localhost:3000/shipments/pending` : Obtiene todos los envios pendientes
2. `POST localhost:3000/shipments` : Crea un nuevo envio con estado pendiente
3. `PUT localhost:3000/shipments/{id}/sent` : Marca un envio como "enviado"
