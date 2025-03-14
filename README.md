# 백엔드(Python)온보딩트랙 파이널 프로젝트

## 코드

### 0. 초기 세팅(허용 사용자, Django APP, CORS 설정)
```python
  # ...

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'books.apps.BooksConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

  # ...
```

### 1. 모델 및 마이그레이션
- models.py
  ```python
  class Book(models.Model):
    book_name = models.CharField(max_length=30, blank=False, default="")
    price = models.DecimalField(max_digits=20, decimal_places=1, blank=False, default=0)
    writer = models.CharField(max_length=30, blank=False, default="")
  ```
- migration 후
  ![image](https://github.com/user-attachments/assets/3185399e-2921-40f7-93d6-2102bc84b023)


### 2. Serializer 생성
- serializer.py
```python
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
```

### 3. View, Url, CRUD 구현
- views.py
```python
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
```
- urls.py
```python
# 만들었던 viewsets을 등록하는 과정
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('book', views.BookViewSet)  # 실제 경로를 바탕으로 api를 주고받을 수 있음

urlpatterns = [
  path('',include(router.urls))
]
```
- BooksApi 내의 urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls'))
]
```

## 구현(API Test)
