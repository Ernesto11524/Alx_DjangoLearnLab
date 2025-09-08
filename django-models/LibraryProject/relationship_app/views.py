from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required

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
    return render(request, "relationship_app/register.html", {"form": form})

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
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")

def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"

@user_passes_test(is_admin, login_url="/no-access/")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian, login_url="/no-access/")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member, login_url="/no-access/")
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required("relationship_app.can_add_book", login_url="/no-access/")
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "add_book.html")

@permission_required("relationship_app.can_change_book", login_url="/no-access/")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "edit_book.html", {"book": book})

@permission_required("relationship_app.can_delete_book", login_url="/no-access/")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "delete_book.html", {"book": book})


# List Books (no permission needed for viewing)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})