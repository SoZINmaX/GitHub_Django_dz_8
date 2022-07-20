from django.urls import path
from . import views

urlpatterns = [
    path('randomstr', views.randomstr, name='randomstr'),
]