from django.shortcuts import render
from app1 .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.models import Student
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request):
    if request.method == "GET":
        id = request.data.get('id')
        print("id",id)
        if id is not None :
            stu = Student.objects.get(id=id)
            print('stu',stu)
            srlzr = Studentserializer(stu)
            print('serlzer',srlzr)
            return Response(srlzr.data)
        else:
            stu = Student.objects.all()
            print("stu",stu)
            srlzer = Studentserializer(stu,many=True)
            print("serlzrt",srlzer)
            return Response(srlzer.data)


    if request.method == "POST":
        data = request.data 
        serilzer = Studentserializer(data=data)
        if serilzer.is_valid():
            serilzer.save()
            return Response({'msg':"data added Successfully "})
        return Response(serilzer.errors)

    if request.method == "PUT" :
        edit_id= request.data.get('id')
        stu = Student.objects.get(id=edit_id)
        serializer = Studentserializer(stu,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data updated"})
        return Response(serializer.errors)


    if request.method == "DELETE":
        del_id = request.data.get('id')
        Student.objects.get(id=del_id).delete()
        return Response({"msg":"delete Successfully"})  


    # if request.method == "PATCH" :
    #     up_data = request.data.get('id')
    #     stu = Student.objects.get(id=up_data)
    #     serializer = Studentserializer(stu,data=request.data,partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg":"Update successfully"})



    




