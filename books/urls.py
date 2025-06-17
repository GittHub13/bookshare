from django.urls import path, include
from .views import home_page, book_list, welcome
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home_page, name='home'),
    path('books/list/', book_list, name='book-list'),
    path('api/', include(router.urls)),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='auth')),
]
