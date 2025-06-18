from rest_framework import serializers
from books.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'genre', 'description',
            'condition', 'status', 'cover_image', 'owner',
            'current_holder', 'created_at', 'updated_at'
        ]