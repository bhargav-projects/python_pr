 
import requests
import json
Base_url='http://127.0.0.1:8000/'
ENDPOINT='api/'
 
#for prticular record
# def get_resource(id):
#     response=requests.get(Base_url+ENDPOINT+id+'/')
#     print(response.status_code)
#     print(response.json())
# id=input('enter id number')
# get_resource(id)  

#session -9  ERROR
def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id,
        }
    response=requests.get(Base_url+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
get_resource(2) 

#! if django not handle error we need to handle error here 
# def get_resource_ErrorHandle(id):
#     response=requests.get(Base_url+ENDPOINT+id+'/')
#     if response.status_code in range(200,300):
#     #if response.status_code == requests.codes.ok:
#         print(response.json())
#     else:
#         print('wrong status code some thing goes wrong')
# id=input('enter id number')
# get_resource_ErrorHandle(id)  


#POST
# def create_resource(): 
#     new_emp={
#         'ename':'bhargav',
#         'enum':127,
#         'eadres':'NYP',
#         'esal':1000,
        
#     }
#     respo=requests.post(Base_url+ENDPOINT,data=json.dumps(new_emp))
#     print(respo.status_code)
#     print(respo.json())
# create_resource()

# #!UPDATE 
# def update_resource(id):
#     new_emp = {
#         'esal':100000,
#         'eadres':'VMP',
        
#     }
#     respo = requests.put(Base_url+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
#     print(respo.status_code)
#     print(respo.json())
# update_resource(2)

# #! DELETE RESOURCE
# def delete_resource():
#     respo = requests.delete(Base_url+ENDPOINT+str(id)+'/')
#     print(respo.status_code)
#     print(respo.json())
# delete_resource()

#output to console is called dumpdata
#py manage.py dumpdata testapp.Emp --indent 4
#py manage.py dumpdata testapp.Emp --format xml --indent 4
#PS E:\dj\restapi\woutapi2ModelCRUD> py manage.py dumpdata testapp.Emp --format xml > EMP.xml --indent 4
#PS E:\dj\restapi\woutapi2ModelCRUD> type EMP.xml