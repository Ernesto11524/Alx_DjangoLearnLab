from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewBooks, name="View_books"),
    path('library', views.LibraryDetailView)
]