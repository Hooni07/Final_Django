# 만들었던 viewsets을 등록하는 과정
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('book', views.BookViewSet)  # 실제 경로를 바탕으로 api를 주고받을 수 있음

urlpatterns = [
  path('',include(router.urls))
]