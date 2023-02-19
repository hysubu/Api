from django.shortcuts import render
from app1 .serilizers import StudentSerilizer
from app1 .models import Student
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework .renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        print("streamdata",stream)
        python_data = JSONParser().parse(json_data)
        print("pythondata",python_data)
        serilizer = StudentSerilizer(data = python_data)
        print("srilzr",serilizer)
        if serilizer.is_valid():
            serilizer.save()
            res = {"msg":'data insert'}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data,content_type='application/json')


# def show(request):
#     s = Student.objects.all()
#     return render(request,'View.html',{"s":s})
