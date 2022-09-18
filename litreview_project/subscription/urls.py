from django.urls import path

from . import views

app_name = 'subscription'

urlpatterns = [
    path('', views.subscription, name='subscription'),
    path('unsubscribe/<user_to_unsubscribe>',
         views.unsubscribe, name='unsubscribe'),
]
