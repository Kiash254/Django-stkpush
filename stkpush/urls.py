from django.urls import path
from .views import landing_page, home, login_view, register_view, dashboard

app_name = 'stkpush'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]