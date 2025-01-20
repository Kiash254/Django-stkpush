from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Card
from .forms import CardForm

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

@login_required
def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card added successfully!')
            return redirect('stkpush:dashboard')
    else:
        form = CardForm()
    return render(request, 'add_card.html', {'form': form})

@login_required
def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card updated successfully!')
            return redirect('stkpush:dashboard')
    else:
        form = CardForm(instance=card)
    return render(request, 'edit_card.html', {'form': form})

@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        card.delete()
        messages.success(request, 'Card deleted successfully!')
        return redirect('stkpush:dashboard')
    return render(request, 'delete_card.html', {'card': card})