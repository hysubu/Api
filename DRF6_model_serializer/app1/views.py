from django.shortcuts import render
from app1 .models import Student
from app1 .serializer import StudentSerializer
from django.views import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
from django .views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class ApiCrud(View):
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            respns_to_clint = {'msg':'data added successfully !!'}
            jsn_data = JSONRenderer().render(respns_to_clint)
            return HttpResponse(jsn_data)
        respns_to_clint = {'msg':'Somthing Wrong !!'}
        jsn_data = JSONRenderer().render(respns_to_clint)
        return HttpResponse(json_data)

