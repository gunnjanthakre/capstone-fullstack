from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dealership', 'purchase', 'car_make', 'car_model', 'sentiment')
    search_fields = ('name', 'review', 'car_make', 'car_model')

