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
```
http://localhost:8000/api/movies/{MOVIE_ID}
```



