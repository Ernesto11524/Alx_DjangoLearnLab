from rest_framework import serializers
from .models import Author, Book

# This is the serializer of the book model.
# It is reposible for serializing the instances of the book model into formats like json and others.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

# This is also the serializer for the Author model. 
# It is reposible for serializing the instances of the author instances together with the books written by them.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer()

    class Meta:
        model = Author
        fields = ['name', 'books',]

# serializers.ValidationError