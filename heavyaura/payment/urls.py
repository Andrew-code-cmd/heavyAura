from django.urls import path
from . import views, webhooks

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='payment_completed'),
    path('process/', views.payment_canceled, name='payment_canceled'),
    path('webhook/', webhooks.stripe_webhook, name='webhook'),
]