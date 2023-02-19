import requests
import json

URL = 'http://127.0.0.1:8000/'
def add_data():
    data = {'name':'subrat mohanty',
    'age':21,
    'city':'Bhubaneswar'}
    header = {'content-Type' :'application/json'}
    json_data = json.dumps(data)
    req_res = requests.post(url=URL,data=json_data,headers=header)
    respns = req_res.json()
    print(respns)

add_data()


URL = 'http://127.0.0.1:8000/'
def view_data(id=None):
    data = {}
    if data is not None :
        data = {'id':id}
    header = {'content-Type' :'application/json'}
    jsn_data = json.dumps(data)
    req_res = requests.get(url=URL,data=jsn_data,headers=header)
    res = req_res.json()
    print(res)

view_data(1)


