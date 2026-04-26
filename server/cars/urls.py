from django.urls import path
from . import views

urlpatterns = [
    path('makes/', views.get_car_makes, name='get_car_makes'),
]