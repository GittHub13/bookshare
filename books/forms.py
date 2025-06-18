from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'genre', 'description',
            'condition', 'status', 'cover_image'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }