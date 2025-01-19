from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Card

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    pin = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'PIN'
    }), max_length=4)

class RegistrationForm(forms.ModelForm):
    pin = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'PIN'
    }), max_length=4)
    confirm_pin = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm PIN'
    }), max_length=4)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("pin")
        confirm_pin = cleaned_data.get("confirm_pin")

        if pin and confirm_pin and pin != confirm_pin:
            raise forms.ValidationError("Pins do not match")
        
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }