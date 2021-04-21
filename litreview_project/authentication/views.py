from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('posts:feed')
        else:
            form = AuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})
    else:
        return redirect('posts:feed')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('authentication:login')

def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('posts:feed')
        else:
            form = UserCreationForm()
        return render(request, 'authentication/registration.html', {'form': form})
    else:
        return redirect('posts:feed')