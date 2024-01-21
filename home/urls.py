from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

urlpatterns = [
    path("", home.as_view(), name="home"),
]
