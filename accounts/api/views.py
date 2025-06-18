from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer