import requests
import json


URL = 'http://127.0.0.1:8000/studentapi/'
def add_data():
    data = {'name':'subrat mohanty',
    'age':21,
    'city':'Bhubaneswar'}
    header = {'content-Type' :'application/json'}
    json_data = json.dumps(data)
    req_res = requests.post(url=URL,data=json_data,headers=header)
    respns = req_res.json()
    print(respns)

# add_data()


URL = 'http://127.0.0.1:8000/studentapi/'
def view_data(id=None):
    data = {}
    if data is not None :
        data = {'id':id}
    header = {'content-Type' :'application/json'}
    jsn_data = json.dumps(data)
    req_res = requests.get(url=URL,data=jsn_data,headers=header)
    res = req_res.json()
    print(res)

# view_data()




URL = 'http://127.0.0.1:8000/studentapi/'
def update_data():
    data = {
        'id':2,
        'name':'subu',
        'age':22
    }
    
    header = {'content-Type' :'application/json'}
    jsn_data = json.dumps(data)
    req_res = requests.put(url=URL,data=jsn_data,headers=header)
    res = req_res.json()
    print(res)

# update_data()



URL = 'http://127.0.0.1:8000/studentapi/'
def delete_data(id):
    data = {
       "id":id
    }
    header = {'content-Type' :'application/json'}
    jsn_data = json.dumps(data)
    req_res = requests.delete(url=URL,data=jsn_data,headers=header)
    res = req_res.json()
    print(res)

delete_data(3)


URL = 'http://127.0.0.1:8000/studentapi/'
def patch_data():
    data = {
       "id":9,
       "name":"subrat mohanty",
       "age":21,
       "city" : "Odisha"
    }
    header = {'content-Type' :'application/json'}
    jsn_data = json.dumps(data)
    req_res = requests.patch(url=URL,data=jsn_data,headers=header)
    res = req_res.json()
    print(res)

patch_data()


