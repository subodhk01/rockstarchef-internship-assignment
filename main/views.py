from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.core import serializers
from django.db.models.functions import Lower
from .models import Movie
from .serializers import MovieSerializer
import json

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def order_movies(request, order_by):
    if not request.user.is_authenticated:
        return HttpResponse('Permission denied, you need to login first')
    try:
        movies = Movie.objects.all().order_by(Lower(order_by))
        movie_list = []
        for movie in movies:
            movie_list.append({
                "id" : movie.id,
                "name" : movie.name,
                "time_created" :  str(movie.time_created),
                "rating" : movie.rating
            })
        movie_list = json.dumps(movie_list)
        return HttpResponse(movie_list, content_type="text/json-comment-filtered")
    except:
        return HttpResponse('Invalid Query')

@csrf_exempt
def user_login(request):
    if request.user.is_authenticated :
        return HttpResponse('Already Logged in')
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return HttpResponse('Invalid Request - include "username" and "password" in the request body')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login Successfull')
        else:
            return HttpResponse('Invalid Credential')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def user_register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return HttpResponse('Invalid Request - include "username" and "password" in the request body')
        try:
            email = request.POST['email']
        except:
            email = ""
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user_auth = authenticate(request, username=username, password=password)
            if user is not None:
                return HttpResponse("Signup Successful")
            else:
                return HttpResponse('Unable to Signup, try again')
        except:
            return HttpResponse('Username already exists')
    else: 
        return HttpResponse('Invalid Request')

@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponse('User Logged out')
