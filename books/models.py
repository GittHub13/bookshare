from django.db import models
from authentication.models import CustomUser


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('given', 'Given'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    interested_users = models.ManyToManyField(CustomUser, related_name='interested_books', blank=True)
    selected_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='selected_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isbn = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"


