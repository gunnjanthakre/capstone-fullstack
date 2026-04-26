from django.contrib import admin
from .models import Dealer

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'city', 'state', 'zip')
    search_fields = ('full_name', 'city', 'state')

