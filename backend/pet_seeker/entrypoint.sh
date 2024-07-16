#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations --merge
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Tests..."
python manage.py test

echo "Create super user..."
python manage.py createsuperuser --noinput

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000