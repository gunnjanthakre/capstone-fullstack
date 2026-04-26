from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Dealer

@require_http_methods(["GET"])
def get_dealerships(request):
    dealers = list(Dealer.objects.values())
    return JsonResponse({'dealers': dealers})

@require_http_methods(["GET"])
def get_dealership(request, dealer_id):
    dealer = Dealer.objects.filter(id=dealer_id).values().first()
    if dealer:
        return JsonResponse(dealer)
    return JsonResponse({'error': 'Dealer not found'}, status=404)

@require_http_methods(["GET"])
def get_dealerships_by_state(request, state):
    dealers = list(Dealer.objects.filter(state__iexact=state).values())
    return JsonResponse({'dealers': dealers})
