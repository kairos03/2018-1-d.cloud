#!/bin/bash
rm -f db.sqlite3
rm -r restful/migrations
python manage.py makemigrations restful
python manage.py migrate
