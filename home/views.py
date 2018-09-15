from django.shortcuts import render
from django.http import HttpResponse





def home (request, username):
    return HttpResponse('home detail page return the id of {username}')