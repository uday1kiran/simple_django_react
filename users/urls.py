from django.urls import path
from .views import hello

urlpatterns = [
    path('hello', hello),
    path('hello1', hello1),
]
