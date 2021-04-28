from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Model
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import UserFollows

@login_required
def subscription(request):
    context = {'error': None, 'user_follows': UserFollows.objects.all()}
    
    if request.method == 'POST':
        username_to_follow = request.POST.get('username')
        try:
            new_follow = User.objects.get(username=username_to_follow)
        except User.DoesNotExist:
            context['error'] = 'Cet utilisateur n\'existe pas !'
        else:
            if new_follow == request.user:
                context['error'] = 'C\'est impossible de s\'abonner à soi-même !'
            else:
                try:
                    uf = UserFollows(user=request.user, followed_user=new_follow)
                except IntegrityError:
                    context['error'] = 'Vous êtes déjà abonné à cet utilisateur !'
                else:
                    uf.save()
    
    return render(request, 'subscription/subscription.html', context)

@login_required
def unsubscribe(request, user_to_unsubscribe):
    try:
        user_to_unsubscribe = User.objects.get(username=user_to_unsubscribe)
    except User.DoesNotExist:
        pass
    else:
        for uf in UserFollows.objects.all():
            if uf.user == request.user and uf.followed_user == user_to_unsubscribe:
                uf.delete()

    return redirect('subscription:subscription')