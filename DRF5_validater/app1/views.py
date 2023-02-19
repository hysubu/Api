from django.shortcuts import render
from django.views import View
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from app1 .serializer import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators .csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Crudapi(View):
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = Studentserializer(data = py_data)
        if serializer.is_valid():
            serializer.save()
            req_res ={"msg":'data Added Successfully !!'} 
            jsn_d = JSONRenderer().render(req_res)
            return HttpResponse(jsn_d)
        jsn_d = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsn_d) 


