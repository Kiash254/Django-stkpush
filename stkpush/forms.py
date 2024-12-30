from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    pin = forms.CharField(widget=forms.PasswordInput, max_length=4)

class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    pin = forms.CharField(widget=forms.PasswordInput, max_length=4)
    confirm_pin = forms.CharField(widget=forms.PasswordInput, max_length=4)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'pin', 'confirm_pin']

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("pin")
        confirm_pin = cleaned_data.get("confirm_pin")

        if pin and confirm_pin and pin != confirm_pin:
            raise forms.ValidationError("Pins do not match")