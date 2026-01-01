#!/bin/bash

# Exit on error,
set -e

# Prints ecah command before executing it
set -x

echo "this is a test run to see if everything is ok!"
echo "Setting up Django development environment..."

echo "Deleting old migration stuff, strating fresh..."
rm -rf core/migrations/*
touch core/migrations/__init__.py

python manage.py makemigrations

# Apply migrations
echo "Applying migrations..."
python manage.py migrate


echo "Starting Django server..."
echo "dev environment up and running"
python manage.py runserver 0.0.0.0:8000
