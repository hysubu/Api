from django.shortcuts import render
import io
from rest_framework .parsers import JSONParser
from app1.serializer import StudentSerializer
from app1 .models import Student
from rest_framework .renderers import JSONRenderer
from django .http import HttpResponse
from django .views.decorators.csrf import csrf_exempt
import requests
import json




# <<<<<<<<<<<< Add data /Post Data >>>>>>>>>>>>>>>>>

@csrf_exempt
def add_api(request):
    if request.method == "POST" :
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) 
        serilzr_data = StudentSerializer(data= py_data)
        if serilzr_data.is_valid():
            serilzr_data.save()
            respons_to_clint = {'msg':'data Added Successfully !!'}
            json_data = JSONRenderer().render(respons_to_clint)
            return HttpResponse(json_data)

  # <<<<<<<<<<<<<<<<<<<<<<<<View Data >>>>>>>>>>>>>>>>>>...

    if request.method =="GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        v_id = py_data.get('id')
        v_data = Student.objects.get(id = v_id)
        serilizer = StudentSerializer(v_data)
        print("serilizer",serilizer)
        json_dat = JSONRenderer().render(serilizer.data)
        return HttpResponse(json_dat)


# <<<<<<<<<<< Delete Data >>>>>>>>>>>>>>>>>

    # if request.method == 'DELETE' :
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     py_data = JSONParser().parse(stream)
    #     d_data = py_data.get('id')
    #     dlt = Student.objects.get(id=d_data)
    #     dlt.delete()
    #     respns_to_clint = {"msg":"delete Successfull !!"}
    #     jsn_res = JSONRenderer().render(respns_to_clint)
    #     return HttpResponse(jsn_res)


#<<<<<<<<<<<<<<<<<<<<<< Update Data >>>>>>>>>>>>>>>>>>>>

    # if request.method == 'PUT' :
    #     json_d = request.body              # come from all data what is the post a user or api 
    #     streamm = io.BytesIO(json_d)
    #     py_da = JSONParser().parse(streamm)      # convert the data json to python dtaya type 
    #     u_id = py_da.get('id')
    #     stu_id = Student.objects.get(id=u_id)
    #     serializer = StudentSerializer(stu_id,data=py_da,partial=True)
    #     if serializer.is_valid() :
    #         serializer.save()
    #         respon_clint = {"msg":'successfull Updated'}
    #         jsn_dat = JSONRenderer().render(respon_clint)
    #         return HttpResponse(jsn_dat)

def view(request):
    data = Student.objects.all()
    return render(request,'view.html',{"data":data})


def addata(request):
    URL = 'http://127.0.0.1:8000/'
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        city = request.POST['city']
        data = {
            'name':name,
            'age' : age ,
            'city' : city
            }
        jsn_data = json.dumps(data)
        request_response = requests.post(url=URL ,data=jsn_data)
        res = request_response.json()
        print(res)
    return render(request,'Store.html')
        


