from itertools import chain

from django.shortcuts import render, redirect
from django.db.models import CharField, Value

from .models import Ticket, Review
#from ..subscription.models import UserFollows

def feed(request):
    if request.user.is_authenticated:
        #user_subs = [uf.followed_user for uf in UserFollows.objects.all().filter(user=request.user)]
        reviews = Review.objects.all()
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        
        reviewed_tickets_title = [r.ticket.title for r in Review.objects.all()]
        reviewed_tickets = Ticket.objects.filter(title__in=reviewed_tickets_title)
        reviewed_tickets = reviewed_tickets.annotate(content_type=Value('REVIEWED_TICKET', CharField()))
        
        unreviewed_tickets = Ticket.objects.exclude(title__in=reviewed_tickets_title)
        unreviewed_tickets = unreviewed_tickets.annotate(content_type=Value('UNREVIEWED_TICKET', CharField()))
        
        posts = sorted(chain(reviews, reviewed_tickets, unreviewed_tickets), 
                       key=lambda post: post.time_created, reverse=True)

        return render(request, 'posts/feed.html', {'posts': posts})
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