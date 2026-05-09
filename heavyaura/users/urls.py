from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='login'),
    path('profile/', views.profile, name='login'),
    path('logout/', views.logout, name='login'),
]