from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home', index, name='home'),
    path('sobre', sobre, name='sobre'),
    path('servicos', servicos, name='servicos'),
]