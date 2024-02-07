#!/bin/sh

# To update run
pip install --upgrade pip

# Install required packages (change this if needed)
pip install -r requirements/develop.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
