from django.urls import path, include
from . import views as web_views

urlpatterns = [
    # Web views
    path('', web_views.book_list, name='book-list'),
    path('<int:pk>/', web_views.book_detail, name='book-detail'),

    # API views
    path('api/', include('books.api.urls')),
]