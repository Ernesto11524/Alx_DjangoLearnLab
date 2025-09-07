from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('', views.list_books, name="View_books"),
    path('library', views.LibraryDetailView)
]