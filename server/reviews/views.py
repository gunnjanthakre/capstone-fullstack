from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Review

@require_http_methods(["GET"])
def get_reviews(request, dealer_id):
    reviews = list(Review.objects.filter(dealership_id=dealer_id).values())
    return JsonResponse({'reviews': reviews})

@csrf_exempt
@require_http_methods(["POST"])
def analyze_review(request):
    try:
        data = json.loads(request.body)
        review_text = data.get('review', '')
        sentiment = Review.analyze_sentiment(review_text)
        return JsonResponse({'sentiment': sentiment})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
