from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListView.as_view(), name='all-books'),
    path('books/<int:pk>/', views.DeleteView.as_view(),),
    path('create/', views.CreateView.as_view(),),
    path('update/', views.UpdateView.as_view(),),
    path('delete/', views.DeleteView.as_view(),),
]