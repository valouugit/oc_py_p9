from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flux/", views.flux, name="flux"),
    path("follow/", views.follow, name="follow"),
    path("register/", views.register, name="register"),
]
