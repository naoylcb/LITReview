from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('posts/', views.posts, name='posts'),
    path('create/ticket', views.create_ticket, name='create_ticket'),
    path('create/review/<ticket_title>',
         views.create_review, name='create_review'),
    path('create/ticket&review', views.create_ticket_review,
         name='create_ticket_review'),
    path('edit/ticket/<ticket_title>', views.edit_ticket, name='edit_ticket'),
    path('delete/ticket/<ticket_title>',
         views.delete_ticket, name='delete_ticket'),
    path('edit/review/<review_headline>',
         views.edit_review, name='edit_review'),
    path('delete/review/<review_headline>',
         views.delete_review, name='delete_review'),
]
