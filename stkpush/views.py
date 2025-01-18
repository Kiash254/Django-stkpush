from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

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
    return render(request, 'dashboard.html')

@login_required
def card_detail(request, card_id):
    # Dummy data for demonstration
    card_details = {
        1: {"title": "Card Title 1", "description": "Detailed description for card 1", "image": "images/avatar-placeholder.png"},
        2: {"title": "Card Title 2", "description": "Detailed description for card 2", "image": "images/avatar-placeholder.png"},
        3: {"title": "Card Title 3", "description": "Detailed description for card 3", "image": "images/avatar-placeholder.png"},
        4: {"title": "Card Title 4", "description": "Detailed description for card 4", "image": "images/avatar-placeholder.png"},
        5: {"title": "Card Title 5", "description": "Detailed description for card 5", "image": "images/avatar-placeholder.png"},
        6: {"title": "Card Title 6", "description": "Detailed description for card 6", "image": "images/avatar-placeholder.png"},
    }
    card = card_details.get(card_id, {})
    return render(request, 'card_detail.html', {'card': card})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('stkpush:login')