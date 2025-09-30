from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('posts/', ListView.as_view()),
    path('post/new/', CreateView.as_view()),
    path('posts/<int:pk>/', DetailView.as_view()),
    path('posts/<int:pk>/edit/', UpdateView.as_view()),
    path('post/<int:pk>/update/', UpdateView.as_view()),
    path('post/<int:pk>/delete/', DeleteView.as_view()),
]

# ["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]
# "tags/<slug:tag_slug>/", "PostByTagListView.as_view()