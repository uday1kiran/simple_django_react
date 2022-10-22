from django.urls import path
from .views import hello1, hello2

urlpatterns = [
    path('hello1', hello1),
    path('hello2', hello2),
]
