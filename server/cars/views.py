from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import CarMake

@require_http_methods(["GET"])
def get_car_makes(request):
    makes = list(CarMake.objects.values())
    return JsonResponse({'makes': makes})
