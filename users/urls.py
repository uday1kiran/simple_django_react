from django.urls import path
from .views import hello, hello1

urlpatterns = [
    path('hello', hello),
    path('hello1', hello1),
]
