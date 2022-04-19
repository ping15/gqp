#!/bin/sh

pipenv run python manager.py migrate
pipenv run python manager.py collectstatic --noinput
pipenv run gunicorn blogproject.wsgi -w 2 -k gthread -b 0.0.0.0:8000 --chdir=/app/

