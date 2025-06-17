from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_kb = 500  # 500KB
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image file size should not exceed {max_size_kb}KB")

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PickupLocation(models.Model):
    name = models.CharField(max_length=255)

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=False, default=1)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=False, default=1)
    pickup_location = models.ForeignKey('PickupLocation', on_delete=models.CASCADE, null=False, default=1)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    cover_image = models.ImageField(
        upload_to='covers/',
        validators=[validate_image_size],
        default='covers/default.jpg'
    )

    interested_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='interested_books', blank=True)
    selected_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='selected_books')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    isbn = models.CharField(max_length=13, null=False, blank=True, default='UNKNOWN')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

