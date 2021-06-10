
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
 **Authentication:**

http://0.0.0.0:8000/api/token/
```http
POST /new_task
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `cmd` | `string` | **Required**. Your command i.e: ls, pwd |

## Responses

```javascript
{
    "id": "609d6d050cc8c94566426202",
    "status": 201
}
```
* List of all Api and Api documentations:

http://0.0.0.0:8000/

