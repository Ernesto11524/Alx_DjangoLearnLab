from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    content = {
        'books' : books
    }
    return render(request, 'relationship_app/list_books.html', content)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"   # you’ll create this
    context_object_name = "library"         # so you can use {{ library }} in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all related books
        context["books"] = self.object.books.all()
        return context
    
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect("/")   # redirect to home page
        messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "registration_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "registration_app/logout.html")
