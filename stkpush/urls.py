from django.urls import path
from . import views

app_name = 'stkpush'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
]