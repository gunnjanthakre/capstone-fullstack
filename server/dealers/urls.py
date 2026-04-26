from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dealerships, name='get_dealerships'),
    path('<int:dealer_id>/', views.get_dealership, name='get_dealership'),
    path('state/<str:state>/', views.get_dealerships_by_state, name='get_dealerships_by_state'),
]