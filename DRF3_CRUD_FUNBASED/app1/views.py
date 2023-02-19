from django.shortcuts import render
from app1.serilizer import StudentSerilizer
from app1 .models import Student
import io
from rest_framework.renderers import JSONRenderer
from rest_framework .parsers import JSONParser
from django.http import HttpResponse
from django .views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def crud_api(request):
    if request.method == 'GET' :
        json_data = request.body
        print("jsondata",json_data)
        stream = io.BytesIO(json_data)
        print("stream",stream)
        python_data = JSONParser().parse(stream)
        print("pyton_data",python_data)
        id = python_data.get('id',None)
        if id is not None :
            stu = Student.objects.get(id=id)
            serilizer = StudentSerilizer(stu)
            j_data = JSONRenderer().render(serilizer.data)
            return HttpResponse(j_data,content_type = 'application/json') 
        
        stu = Student.objects.all()
        serilizer = StudentSerilizer(stu,many=True)
        j_data = JSONRenderer().render(serilizer.data)
        return HttpResponse(j_data,content_type = 'application/json')



#<<<<<<<<<<<< Post Data / Create Data /Insert Data >>>>>>>>>>>>>>>

#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pytho_data = JSONParser().parse(stream)
#         serilizer = StudentSerilizer(data = pytho_data)
#         if serilizer.is_valid():
#             serilizer.save()
#             msg = {"dta":'data posted'}
#             jsn_dat = JSONRenderer().render(msg)
#             return HttpResponse(jsn_dat)


# #<<<<<<<<<<<<<<<<<<<<<<< Update Data >>>>>>>>>>>>>>>>>>>>>>>>>>>>

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         edit_python_data = JSONParser().parse(stream)
#         id = edit_python_data.get('id')
#         stu_dat= Student.objects.get(id=id)
#         serilizer = StudentSerilizer(stu_dat,data= edit_python_data,partial=True)
#         if serilizer.is_valid():
#             serilizer.save()
#             msgg = {"msg":'update Successfully'}
#             jsn_data = JSONRenderer().render(msgg)
#             return HttpResponse(jsn_data)

#     if request.method == 'DELETE' :
#          j_data  = request.body 
#          stream = io.BytesIO(j_data)
#          py_d = JSONParser().parse(stream)
#          d_id = py_d.get('id')
#          q_id = Student.objects.get(id=d_id)
#          q_id.delete()
#          res = {'msg':'delete successfully'}
#          jsoon = JSONRenderer().render(res)
#          return HttpResponse(jsoon,content_by = 'application/json')
