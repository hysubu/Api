import requests
import json



#<<<<<<<<<<<<< Get Data / View  Data >>>>>>>>>>>>>>>>>

URl = 'http://127.0.0.1:8000/'


def get_data(id = None):
    data = {}
    if id is not None :
        data = { "id":id }
    json_data = json.dumps(data)
    req_response = requests.get(url=URl,data=json_data)
    dat = req_response.json()
    # print(dat,type(dat))
    print(req_response,type(req_response))

# get_data(1)




#<<<<<<<<<<<<<<<<<<< Post Data >>>>>>>>>>>>>>>>>>


URl = 'http://127.0.0.1:8000/api/'

def post_data():
    data = {
        'name' : 'sgar',
        'age' : 24,
        'city' : 'bhubaneswar'
        
    }
    jsn_data = json.dumps(data)
    req_res = requests.post(url=URl,data = jsn_data)
    dat = req_res.json()
    print(dat)
    
post_data()



#<<<<<<<<<<<<<<<<< Update Data/ (Put Data) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def update_data():
    data = {
        'id':4,
        "name" : 'arjit sahoohhh',
        'city' : 'india'
    }
    jsn_data = json.dumps(data)
    req_res = requests.put(url=URl,data=jsn_data)
    dat = req_res.json()
    print(dat)

# update_data()


def delet_data() :
    data = {'id':1}
    jsn_data = json.dumps(data)
    req_res = requests.delete(url=URl,data=jsn_data)
    res = req_res.json()
    print(res)

# delet_data()
