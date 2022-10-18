#!/bin/sh

docker exec -it incident_be python3 manage.py migrate
docker exec -it incident_be python3 manage.py populate_db