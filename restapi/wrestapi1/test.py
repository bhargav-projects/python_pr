import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

#----------------#!GET------------------------
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id,
            
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource()

#----------------#!POST------------------------
# def create_resource():
#     new_emp={
#         'ename':'radhaKrishna',
#         'enum':999,
#         'esal':100000,
#         'eadres':'vrindhavan'
#     }
     
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

#----------------#!UPDATE------------------------

# def update(id):
#     new_data={
#         'id':id,
#         'ename':'chakri',
#         'enum':5,
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# update(2)
#----------------#!DELETE------------------------
# def delete(id):
#     data={
#             'id':id,
            
#         }
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete(1)