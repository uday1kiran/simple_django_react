from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def hello():
    return Response('hello')

@api_view(['POST'])
def hello1():
    return Response('hello post test from postman')