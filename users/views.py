from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def hello1(request):
    return Response('hello')
    
@api_view(['POST'])
def hello2(request):
    return Response('hello - POST - test from POSTMAN')
   
