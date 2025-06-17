from django.contrib import admin
from .models import Genre, Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner', 'status')
    list_filter = ('status', 'genre')
    search_fields = ('title', 'author__name')

admin.site.register(Genre)
admin.site.register(Author)
