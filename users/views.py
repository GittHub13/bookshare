from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """User profile view"""
    context = {
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_edit(request):
    """Edit profile view"""
    if request.method == 'POST':
        # Add your form processing logic here
        return redirect('users:profile')

    context = {
        'user': request.user,
    }
    return render(request, 'users/profile_edit.html', context)