#!/bin/bash

echo "Building your project..."

python pip install -r requirements.txt

echo "Creating migrations..."

python manage.py makemigrations --noinput

python manage.py migrate --noinput --clear


