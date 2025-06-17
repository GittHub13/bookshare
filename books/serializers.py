from rest_framework import serializers
from .models import Author
from .models import Book
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'description',
            'owner',
            'author',
            'genre',
            'status',
            'image',
            'pickup_location',
            'interested_users',
            'selected_user',
            'created_at',
            'updated_at',
            'isbn'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']
        extra_kwargs = {
            'image': {'required': False},
            'isbn': {'required': False}
        }

    def to_representation(self, instance):
        """Custom representation for nested relationships"""
        representation = super().to_representation(instance)

        # Convert foreign keys to their string representation
        if instance.author:
            representation['author'] = instance.author.name
        if instance.genre:
            representation['genre'] = instance.genre.name
        if instance.pickup_location:
            representation['pickup_location'] = instance.pickup_location.name

        return representation

    def validate(self, data):
        """Custom validation"""
        if data.get('status') == 'given' and not data.get('selected_user'):
            raise serializers.ValidationError(
                "Cannot mark as 'given' without selecting a user"
            )
        return data