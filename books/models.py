from django.db import models

# Create your models here.
class Book(models.Model):
  book_name = models.CharField(max_length=30, blank=False, default="")
  price = models.DecimalField(max_digits=20, decimal_places=1, blank=False, default=0)
  writer = models.CharField(max_length=30, blank=False, default="")
