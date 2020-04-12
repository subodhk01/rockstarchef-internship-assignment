# Rockstarchef Internship Assignment
This Django project is the Assignment for Internship at RockstarChef submitted on 12th April, 2020

## My custom Movie object
```bash
{ 
    "id": 5,                                         # Auto field, automatically gets created when an object is created
    "name": "through raw data",                      # Name of the Movie
    "time_created": "2020-04-12T10:13:20.589388Z",   # Auto time field, automatically gets created when an obejct is created
    "rating": 5                                      # Any number from 1-5
}
```
# How to run the project
 - Clone the project
 - Create a python virtual environment, if you don't know how to refer https://docs.python.org/3/tutorial/venv.html
 - `pip install -r requirements.txt`
 - `python manage.py createsuperuser`
 - `python manage.py runserver` <br><br>
I have already included a db.sqlite3 file but I case you want to create a new database for your project you can, just don't forget to apply the migrations:
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - and then run the server using `python manage.py runserver` <br><br>
All the APIs require an authenticated user, therefore you may want to consider using the login/signup APIs first.

# List of Auth APIs

## User Login
Send a `POST` request to the following url with request body containing "username" and "password"
```
http://127.0.0.1:8000/user/login
```
## User Signup 
Send a `POST` request to the following url with request body containing "username" and "password"
```
http://127.0.0.1:8000/user/signup
```
## User Logout
Send a `GET` request to the following url 
```
http://127.0.0.1:8000/user/logout
```

# List of Movie APIs

## Create
To Create a new Movie object, send a `POST` request to the follwing url and include fields -  "name" and "rating" in the body of the request.
```
http://localhost:8000/api/movies/
```

## List
To list all the Movie objects send a `GET` http request at:
```
http://localhost:8000/api/movies/
```
To list only a particular Movie object send a `GET` http request at:
```
http://localhost:8000/api/movies/{MOVIE_ID}
```

## Update
To update an existing Movie object, send a `PATCH` http request to the following url and include the fiels to be edited in the body of the request.
```
http://localhost:8000/api/movies/{MOVIE_ID}/
```

## Delete
To delete a particular Movie object, send a `DELETE` http request at the following url:
```bash
http://localhost:8000/api/movies/{MOVIE_ID}/            # Don't forget the trailing backslash
```
## Search query
To Search for a particular movie by - name & rating , search fields can be altered through `main/api_views.py` file. Send a `GET` request with parameter `search` to the follwing url:
```
http://localhost:8000/api/movies
```
## Sorting 
To sort the Movie list, send a `GET` request to the following url, wherer `{ORDER_BY}` is the name of field by which you want to sort the list
```
http://localhost:8000/api/movies/order/{ORDER_BY}
```



