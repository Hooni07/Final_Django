from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer