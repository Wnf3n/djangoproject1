from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.display,name='index'),
    path('inicio',views.inicio,name='inicio'),
    path('ver',views.ver,name='ver')
]