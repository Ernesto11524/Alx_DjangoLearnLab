import django_filters
from .models import Author, Book

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['name',]

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']