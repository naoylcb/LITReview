from itertools import chain

from django.shortcuts import render, redirect
from django.db.models import CharField, Value
from django.apps import apps as django_apps

from .models import Ticket, Review
from subscription.models import UserFollows

def feed(request):
    if request.user.is_authenticated:
        users = [uf.followed_user for uf in UserFollows.objects.filter(user=request.user)]
        users.append(request.user)
        
        reviews = Review.objects.filter(user__in=users)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        
        reviewed_tickets_title = [r.ticket.title for r in Review.objects.all()]
        reviewed_tickets = Ticket.objects.filter(user__in=users, title__in=reviewed_tickets_title)
        reviewed_tickets = reviewed_tickets.annotate(content_type=Value('REVIEWED_TICKET', CharField()))
        
        unreviewed_tickets = Ticket.objects.filter(user__in=users).exclude(title__in=reviewed_tickets_title)
        unreviewed_tickets = unreviewed_tickets.annotate(content_type=Value('UNREVIEWED_TICKET', CharField()))
        
        posts = sorted(chain(reviews, reviewed_tickets, unreviewed_tickets), 
                       key=lambda post: post.time_created, reverse=True)

        return render(request, 'posts/feed.html', {'posts': posts})
    else:
        return redirect('authentication:login')
    
def posts(request):
    if request.user.is_authenticated: 
        reviews = Review.objects.filter(user=request.user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        
        tickets = Ticket.objects.filter(user=request.user)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        
        posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

        return render(request, 'posts/posts.html', {'posts': posts})
    else:
        return redirect('authentication:login')

def create_ticket(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.POST.get('image')
            
            ticket = Ticket(title=title, description=description, image=image, user=request.user)
            ticket.save()
            
            return redirect('posts:feed')
        else:
            return render(request, 'posts/create_ticket.html')
    else:
        return redirect('authentication:login')
    
def create_review(request, ticket_title):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(title=ticket_title)
        if request.method == 'POST':
            headline = request.POST.get('headline')
            body = request.POST.get('body')
            rating = request.POST.get('rating')
            
            review = Review(headline=headline, body=body, rating=rating, ticket=ticket, user=request.user)
            review.save()
            
            return redirect('posts:feed')
        else:
            return render(request, 'posts/create_review.html', {'ticket': ticket})
    else:
        return redirect('authentication:login')

def create_ticket_review(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.POST.get('image')
            
            ticket = Ticket(title=title, description=description, image=image, user=request.user)
            ticket.save()
            
            headline = request.POST.get('headline')
            body = request.POST.get('body')
            rating = request.POST.get('rating')
            
            review = Review(headline=headline, body=body, rating=rating, ticket=ticket, user=request.user)
            review.save()
            
            return redirect('posts:feed')
        else:
            return render(request, 'posts/create_ticket_review.html')
    else:
        return redirect('authentication:login')
    
def edit_ticket(request, ticket_title):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(title=ticket_title)
        if request.method == 'POST':
            ticket.title = request.POST.get('title')
            ticket.description = request.POST.get('description')
            ticket.image = request.POST.get('image')
            ticket.save()
            
            return redirect('posts:posts')
        else:
            return render(request, 'posts/edit_ticket.html', {'ticket': ticket})
    else:
        return redirect('authentication:login')

def delete_ticket(request, ticket_title):
    try:
        ticket = Ticket.objects.get(title=ticket_title)
    except Ticket.DoesNotExist:
        pass
    else:
        if request.user == ticket.user:
            ticket.delete()
    finally:
        return redirect('posts:posts')

def edit_review(request, review_headline):
    if request.user.is_authenticated:
        review = Review.objects.get(headline=review_headline)
        if request.method == 'POST':
            review.headline = request.POST.get('headline')
            review.body = request.POST.get('body')
            review.rating = request.POST.get('rating')
            review.save()
            
            return redirect('posts:posts')
        else:
            return render(request, 'posts/edit_review.html', {'review': review})
    else:
        return redirect('authentication:login')

def delete_review(request, review_headline):
    try:
        review = Review.objects.get(headline=review_headline)
    except Review.DoesNotExist:
        pass
    else:
        if request.user == review.user:
            review.delete()
    finally:
        return redirect('posts:posts')