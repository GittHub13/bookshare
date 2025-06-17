from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from books.models import Book, Genre
from books.serializers import BookSerializer, AuthorSerializer
from .models import Author
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .serializers import GenreSerializer
from django.http import JsonResponse


@login_required
def profile(request):
    # Get the user's profile
    user_profile = get_object_or_404(Profile, user=request.user)

    context = {
        'profile': user_profile,
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)

def home_page(request):
    return render(request, 'home.html')

def book_list(request):
    # აქ დაამატეთ ლოგიკა წიგნების სიისთვის
    return render(request, 'books/list.html')

def welcome():
    return JsonResponse({
        'message': 'Welcome to Book Share API',
        'endpoints': {
            'swagger': '/swagger/',
            'redoc': '/redoc/',
            'api_root': '/api/',
            'admin': '/admin/',
            'auth': '/api/auth/'
        }
    })


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()  # This allows DRF to auto-detect basename
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


