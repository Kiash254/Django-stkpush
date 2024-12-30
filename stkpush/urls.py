from django.urls import path
from .views import home

app_name = 'stkpush'

urlpatterns = [
    path('', home, name='home'),
]