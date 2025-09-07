from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.
def viewBooks(request):
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