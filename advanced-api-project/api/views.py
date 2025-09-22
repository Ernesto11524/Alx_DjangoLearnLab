from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .filters import AuthorFilter, BookFilter

# Create your views here.

class ListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = AuthorFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

class DetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AuthorFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# @IsAuthenticated
class CreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # serializer_class.validate()
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AuthorFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# @IsAuthenticated
class UpdateView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # serializer_class.validate()
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AuthorFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# @IsAuthenticated
class DeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AuthorFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# isAuthenticated