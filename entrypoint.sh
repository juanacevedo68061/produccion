#!/bin/sh

python manage.py collectstatic --no-input

gunicorn General.wsgi:application --bind 0.0.0.0:8000
