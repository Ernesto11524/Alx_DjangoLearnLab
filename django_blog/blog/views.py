from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    return render(request, 'blog/registration.html', {'form' : form})

def profile(request):
    form = CustomUserChangeForm()
    return render(request, 'blog/profile.html', {'form': form})