from django.urls import path
from . import views
from . import authentication

app_name = 'stkpush'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', authentication.login_view, name='login'),
    path('register/', authentication.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('logout/', authentication.logout_view, name='logout'),
]