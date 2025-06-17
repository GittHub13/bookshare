from django.urls import path, include
from .views import home_page, book_list, welcome
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    # Root URLs
    path('', welcome, name='welcome'),
    path('home/', home_page, name='home'),  # Changed from root to '/home/'
    path('books/list/', book_list, name='book-list'),  # More specific path

    # API endpoints
    path('api/', include(router.urls)),  # Grouped under /api/ prefix

    # Authentication
    path('auth/', include('authentication.urls', namespace='auth')),  # Added namespace
]