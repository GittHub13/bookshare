from django.contrib import admin
from authentication.models import CustomUser
from books.models import Genre, Author, Book
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner', 'status')
    list_filter = ('status', 'genre')
    search_fields = ('title', 'author__name')


admin.site.register(Genre)
admin.site.register(Author)
