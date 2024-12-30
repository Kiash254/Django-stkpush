from django.urls import path
from .views import home, login_view, register_view, dashboard

app_name = 'stkpush'

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]