from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    profile_picture = forms.ImageField()
    bio = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']