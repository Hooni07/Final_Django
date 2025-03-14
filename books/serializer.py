# python 객체 -> json 형태로 반환
from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Book
    fields = (
      "id",
      'book_name',
      'price',
      'writer'
    )