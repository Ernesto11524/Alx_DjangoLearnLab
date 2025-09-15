from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView





urlpatterns = [
    path('', views.list_books, name="View_books"),
    path('library', views.LibraryDetailView),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('admins view/', views.admin_view, name='admins'),
    path('librarian/', views.librarian_view, name='libriarian'),
    path('member/', views.member_view, name='member'),
    path("books/", views.book_list, name="book_list"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),
]