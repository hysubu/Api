from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework .response import Response

# Create your views here.

@api_view(['GET','POST'])  # by default method will 
def hello_world(request):
    if request.method == 'GET' :
        print(request.data)
        return Response({'msg':'This is get request'})


    if request.method == 'POST' :
        print(request.data)
        a = request.data 

        return Response({'msg':'This is post request',"request.data":a})



