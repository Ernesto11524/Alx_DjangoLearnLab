from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")

    list_filter = ("author", "publication_year")

    search_fields = ("title", "author")

class CustomUserAdmin(UserAdmin):
    # This is where the code goes

    def nothing(self):
        return None
    
admin.site.register(CustomUser, CustomUserAdmin)