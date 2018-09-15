from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # home/

    # home/71
    path('home/<slug:username>/', views.home)
]
