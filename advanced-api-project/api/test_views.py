from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .models import Book, Author
from . import views
from rest_framework import status

# self, class, APITestCase
# response.data
# self.client.login