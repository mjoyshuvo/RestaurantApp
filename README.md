
Prerequisite
------------

* [Python]
* [Docker]

Getting started
---------------

Git clone and go to the RestaurantApp folder.

* Build using Docker container.
```bash
$ docker-compose build
```
* Run using Docker container.
```bash
$ docker-compose up
```
* Run migration command
```bash
$ docker-compose exec web python manage.py migrate
```
* Create a superuser and necessary roles and permissions for Role based access control i.e: Employee, Restaurant user.
```bash
$ docker-compose exec web python manage.py loaddata import_sql/bootup.json
```

* User credentials:
```bash
username: admin
password: 1q2w3e4r5t6y
```
# Required Api lists:
I used JWT for token based authentication and Role Based Access Control.

* Postman Collection:
  
https://www.getpostman.com/collections/174c454c15c772b00fae

Import this link to postman to get all API required.

* You can also find the list of all Api and Api documentations:

http://0.0.0.0:8000/

* Automated tests:
Some automated tests ate at apps/tests folder
  
```bash
docker-compose exec web python manage.py test
```

* Logs:
Logs are recorded for voting. Logs can be found in apps/log directory. Date wise logs will be there.
