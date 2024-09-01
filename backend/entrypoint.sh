#!/bin/sh

cd /code/pet_seeker

echo "Creating Migrations..."
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

uwsgi --socket :8000 --module pet_seeker.wsgi --chmod-socket=666 --buffer-size 65536
