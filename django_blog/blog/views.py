from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm, PostForm
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        form.save()
    else:
        form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form' : form})

def profile(request):
    form = CustomUserChangeForm()
    return render(request, 'blog/profile.html', {'form': form})

class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    template_name = 'blog/listview.html'

class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()

def updatePost(request, pk):
    post = generics.get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = Post(instance = post)

# LoginRequiredMixin 
# UserPassesTestMixin