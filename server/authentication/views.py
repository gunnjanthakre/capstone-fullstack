from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

@csrf_exempt
@require_http_methods(["POST"])
def login_user(request):
    """Login user"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'username': user.username})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def logout_user(request):
    """Logout user"""
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

@csrf_exempt
@require_http_methods(["POST"])
def register_user(request):
    """Register new user"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return JsonResponse({'message': 'Registration successful', 'user_id': user.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
