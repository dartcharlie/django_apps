preparation:
install mysql locally
create username zhifei and use password in settings.py
create database zsite

python manage.py migrate
python manage.py runserver