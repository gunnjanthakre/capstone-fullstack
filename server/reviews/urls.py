from django.urls import path
from . import views

urlpatterns = [
    path('<int:dealer_id>/', views.get_reviews, name='get_reviews'),
    path('analyze/', views.analyze_review, name='analyze_review'),
]