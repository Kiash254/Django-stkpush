from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card

def landing_page(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    cards = Card.objects.all()
    return render(request, 'dashboard.html', {'cards': cards})

@login_required
def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, 'card_detail.html', {'card': card})