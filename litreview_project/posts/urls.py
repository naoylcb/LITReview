from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('create/ticket', views.create_ticket, name='create_ticket'),
    path('create/review/<ticket_title>', views.create_review, name='create_review'),
    path('create/ticket&review>', views.create_ticket_review, name='create_ticket_review'),
]