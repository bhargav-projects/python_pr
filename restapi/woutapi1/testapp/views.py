from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def woutapi_view(request):
#     emp={
#         'ename':'bhargav',
#         'enum':1,
#         'esal':100,
        
#     }
#     # response='employee name:{} employenumber:{} employeesalary:{}'.format(emp['ename'],
#     #                                                                     emp['enum'],
#     #                                                                     emp['esal'])
#     return HttpResponse(response)

import json
# def json_view(request):
#     emp={
#         'ename':'bhargav',
#         'enum':1,
#         'esal':100,
        
#     }
#     #dumps:cnvrt py obj -json understandble form
#     #loads: cnvrt json - to py understand form
#     json_data = json.dumps(emp)
#     return HttpResponse(json_data,content_type='application/json')


#NEWLY ADDED 
# from django.http import JsonResponse
# def json_view(request):
#     emp={
#         'ename':'bhargav',
#         'enum':1,
#         'esal':100,
        
#     }
#     return JsonResponse(emp)

#CLASS BASED VIEWS =================================
#based on the response correspond method will execute so
#in apis mostly used cbvs

from django.http import JsonResponse
# class JsonCBView(View):
#     #we can pass any no of arguments like emp by using *args
#     def get(self, request,*args, **kwargs):
#         emp={
#             'name':'bhargav',
#             'enum':1,
#             'esal':100,
#         }
#         return JsonResponse(emp)

# class JsonCBView(View):
#     #we can pass any no of arguments like emp by using *args
#     def get(self, request,*args, **kwargs):
    #     json_data=json.dumps({'msg':': hi this is get method json message'})
    #     return HttpResponse(json_data,content_type='application/json')
    # def post(self, request,*args, **kwargs):
    #     json_data=json.dumps({'msg':': hi this post method json message'})
    #     return HttpResponse(json_data,content_type='application/json')
    # def put(self, request,*args, **kwargs):
    #     json_data=json.dumps({'msg':': hi is put methodjson message'})
    #     return HttpResponse(json_data,content_type='application/json')
    # def delete(self, request,*args, **kwargs):
    #     json_data=json.dumps({'msg':': hi is delete methodjson message'})
    #     return HttpResponse(json_data,content_type='application/json')
    
        
#USING MIXIN


from django.views.generic import View
from .mixins import  HttpResponseMixin
class JsonMixinCBV(JsonHttpResponse,View):
    def get(self, request, *args):
        json_data=json.dumps({'msg':': hi this is get method json message'})
        return self.return_to_httpResponse(json_data)
    def post(self, request, *args):
        json_data=json.dumps({'msg':': hi this is post method method json message'})
        return self.return_to_httpResponse(json_data)
    def put(self, request, *args):
        json_data=json.dumps({'msg':': hi this is update method json message'})
        return self.return_to_httpResponse(json_data)
    def delete(self, request, *args):
        json_data=json.dumps({'msg':': hi this is delete method json message'})
        return self.return_to_httpResponse(json_data)
