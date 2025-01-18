from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from .models import Card

def landing_page(request):
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pin = form.cleaned_data['pin']
            user = authenticate(request, username=username, password=pin)
            if user is not None:
                login(request, user)
                return redirect('stkpush:dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['pin'])
            user.save()
            return redirect('stkpush:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

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

def logout_view(request):
    logout(request)
    return redirect('stkpush:login')