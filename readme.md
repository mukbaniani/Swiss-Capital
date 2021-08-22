# Instalation on docker

### docker-compose up

enter django bash

### docker exec -it django bash

change directory

### swisscapital_management

make migrations

### python3 manage.py makemigrations

create migrate

### python3 manage.py migrate

create super user

### python3 manage.py createsuperuser

create dummy departments

### python3 manage.py create_department

create dummy personal quality

### python3 manage.py create_quality

create dummy employee

### python3 manage.py create_employee

[visit](http://127.0.0.1:8000/)

[admin-page](http://127.0.0.1:8000/admin)

# Instanation local machine

** requirements **

- python 3.6, 3.7, 3.8, 3.9

create virtual enviroment

### python3 -m venv vevn

activate virtual enviroment for linux or mac

### source venv/bin/activate

activate virtual enviroment for windows

### venv\Scripts\Activate.bat

install packages

### pip3 install -r requirements.txt

create migrate

### python3 manage.py migrate

create super user

### python3 manage.py createsuperuser

create dummy departments

### python3 manage.py create_department

create dummy personal quality

### python3 manage.py create_quality

create dummy employee

### python3 manage.py create_employee

run server

### python3 manage.py runserver

[visit](http://127.0.0.1:8000/)

[admin-page](http://127.0.0.1:8000/admin)
