from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True) 

class CustomUserManager(BaseUserManager):
    # Hello

    def create_user(self, email, username, password, date_of_birth=None, profile_photo=None):
        # This is where the code goes
        return None

    def create_superuser(self, email, username, password, date_of_birth=None, profile_photo=None):
        return None
    
    class Meta:
        permissions = [
            ('can_view', 'can_view'),
            ('can_create', 'can_create'),
            ('can_edit', 'can_edit'),
            ('can_delete', 'can_delete'),
        ]