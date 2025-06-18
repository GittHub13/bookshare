from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_kb = 500
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image file size should not exceed {max_size_kb}KB.")

User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Condition choices
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('taken', 'Taken'),
    ]

    # Core fields
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    # Condition and status fields
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='good'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    # Ownership fields
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_books'
    )
    current_holder = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='held_books'
    )

    # Additional fields
    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title