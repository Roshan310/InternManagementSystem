from atexit import register
from operator import index
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='Task'),
    path('register/', views.register, name='register'),
    path('login', views.login_view, name='login_view')
]