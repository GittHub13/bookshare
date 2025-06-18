from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #
            return redirect('home')
        else:
            print(form.errors)  #
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'accounts/login.html')

def logout_view(request):
    """User logout view"""
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    profile_picture_url = None
    if user.profile_picture and hasattr(user.profile_picture, 'url'):
        profile_picture_url = user.profile_picture.url

    return render(request, 'profile.html', {'profile_picture_url': profile_picture_url, 'user': user})
