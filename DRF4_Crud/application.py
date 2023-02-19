import requests
import json

# Create your models here.
# URL = 'https://jsonplaceholder.typicode.com/users'
URL = "http://localhost:1234/emp"

# def add_data():
#     data = {
#         'name':'subrat mmmm',
#         'age' : 21 ,
#         'city' : 'Odisha'
#     }
#     jsn_data = json.dumps(data)
#     request_response = requests.post(url=URL ,data=jsn_data)
#     res = request_response.json()
#     print(res)

# add_data()



def view_data(id):
    data = {'id':id}
    json_data = json.dumps(data)
    requ_res = requests.get(url=URL,data=json_data)
    res = requ_res.json()
    print(res)

view_data(6)

def delet_data(id):
    data = {"id":id}
    jsn_data = json.dumps(data)
    request_response = requests.delete(url=URL,data=jsn_data)
    res = request_response.json()
    print(res)

# delet_data(2)


# 
def Update_data():
    data = {
        'id':4,
        'name':'rajesh ku sahh00',
        'age':21,
        'city':'bhubaneswar',
    }
    json_dat = json.dumps(data)
    req_res = requests.put(url=URL,data=json_dat)
    res = req_res.json()
    print(res)

# Update_data()