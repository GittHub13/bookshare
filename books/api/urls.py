from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]