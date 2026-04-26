from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from dealers.models import Dealer
from reviews.models import Review
from cars.models import CarMake


def home_view(request):
    state = request.GET.get('state')
    if state:
        dealers = Dealer.objects.filter(state__iexact=state)
    else:
        dealers = Dealer.objects.all()
    return render(request, 'home.html', {'dealers': dealers, 'state': state})


def dealer_detail(request, dealer_id):
    dealer = Dealer.objects.filter(id=dealer_id).first()
    if not dealer:
        return render(request, 'dealer_detail.html', {'error': 'Dealer not found'})
    reviews = dealer.reviews.all()
    return render(request, 'dealer_detail.html', {'dealer': dealer, 'reviews': reviews})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


def add_review(request, dealer_id):
    dealer = Dealer.objects.filter(id=dealer_id).first()
    if not dealer:
        return render(request, 'add_review.html', {'error': 'Dealer not found'})

    if request.method == 'POST':
        name = request.POST.get('name')
        review_text = request.POST.get('review')
        purchase = request.POST.get('purchase') == 'on'
        purchase_date = request.POST.get('purchase_date') or None
        car_make = request.POST.get('car_make')
        car_model = request.POST.get('car_model')
        car_year = request.POST.get('car_year') or None
        sentiment = Review.analyze_sentiment(review_text or '')

        Review.objects.create(
            name=name or 'Anonymous',
            dealership=dealer,
            review=review_text or '',
            purchase=purchase,
            purchase_date=purchase_date,
            car_make=car_make,
            car_model=car_model,
            car_year=int(car_year) if car_year else None,
            sentiment=sentiment,
        )
        messages.success(request, 'Review added successfully.')
        return redirect('dealer_detail', dealer_id=dealer_id)

    makes = CarMake.objects.all()
    return render(request, 'add_review.html', {'dealer': dealer, 'makes': makes})


def about_page(request):
    return redirect('/static/About.html')


def contact_page(request):
    return redirect('/static/Contact.html')
