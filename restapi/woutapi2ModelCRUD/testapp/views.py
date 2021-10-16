from django.shortcuts import render
from .models import Emp

from django.http import HttpResponse
from django.views.generic import View


from .mixin import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .utils import is_json
from .forms import EmpForm
import json

'''the process converting an object from one
form to another form is called serialization
  ex=pydict-jsonobj ,json-py'''

from django.views.decorators.csrf import csrf_exempt #!method or function level               
from django.utils.decorators import method_decorator  #!class level

from django.core.serializers import serialize
# import json

#! CRUD*--
# !      Retreive operation-- --------- 
# class EmployeeDetailCBV(View):
#     def get(self, request, *args, **kwargs):
#         emp=Emp.objects.get(id=1)#2,3,4,
#         emp_data={
#         'ename':emp.ename,
#         'enum':emp.enum,
#         'edres':emp.eadres,
#         'esal':emp.esal,
#     }
#         json_data=json.dumps(emp_data)
#         return HttpResponse(json_data,'application/json')
    
#  ?client entering id

# CONVERTING QS INTO JSON using -(#!SERIALIZE)
#     # def get(self,id, request,pk, *args, **kwargs):
#     #     emp_data=Emp.objects.get(id=pk)
#           emp_data=serialize('json',qs)
# #!------get all data() 
            #qs=Emp.objects.all()
            #emp_data=serialize('json',[qs])
#     #     return HttpResponse(emp_data,'application/json')



# #?------GET ONLY LIST OF DICTIONARIES AND PARTICULAR FIEDLS
# class EmployeeDetailCBV(View):
#     def get(self, request,*args, **kwargs):
#         qs=Emp.objects.all()
#         json_data=serialize('json',qs,fields=('ename','eadres'))
#         p_data=json.loads(json_data)
#         final_data=[]
#         for obj in p_data:
#             emp_data=obj['fields']
#             final_data.append(emp_data)
#         json_data=json.dumps(final_data)
#         return HttpResponse(json_data,'application/json')
    
#from  .mixin import SerializeMixin,HttpResponseMixin
#                 !USING MIXIN CLASS
# class EmployeeDetailCBV(View,SerializeMixin):
#     def get(self, request,pk, *args, **kwargs):
#         emp=Emp.objects.get(id=pk)
#         json_data=self.Serialize([emp,])
#         return HttpResponse(json_data,'application/json')


#class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    # def get(self, request,*args, **kwargs):
    #     qs=Emp.objects.all()
    #     json_data=self.Serialize(qs)
    #     return HttpResponse(json_data,'application/json')

 
    

#! EXCEPTION HANDLING
# import json
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#     def get(self, request,pk, *args, **kwargs):
#         try:
#             emp=Emp.objects.get(id=pk)
#         except Emp.DoesNotExist:
#             json_data=json.dumps({'msg':'this page doesnt exist'}) 
#             #return HttpResponse(json_data,'application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data=self.Serialize([emp,])
#             #return HttpResponse(json_data,'application/json',status=200)
#             return self.render_to_http_response(json_data)
    
        #! if we cant handle error here go to test.py line 15
        # emp=Emp.objects.get(id=pk)
        # json_data=self.Serialize([emp,])
        # return HttpResponse(json_data,'application/json',status=200)


# Disabling  #!CSRF_TOKEN 

# from .mixin import SerializeMixin,HttpResponseMixin
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from .utils import is_json
# from .forms import EmpForm

# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#     def get(self, request,*args, **kwargs):
#         qs=Emp.objects.all()
#         json_data=self.Serialize(qs)
#         return HttpResponse(json_data,'application/json')

#     def post(self, request,*args, **kwargs):
#         # json_data=json.dumps({'msg':'this is post json data'})
#         # return self.render_to_http_response(json_data,status=200)
        
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'please provide valid json data'})
#             return self.render_to_http_response(json_data,status=404)
#         json_data=json.dumps({'msg':'you provided valid data'})
#         return self.render_to_http_response(json_data,status=200)

# #!if we want to store partener sending data in db we definitely required modelforms 

#         emp_data =json.loads(valid_json)
#         form=EmpForm(emp_data)
#         if form.is_valid():
#             form.save()
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'this data creted successfully'})
#             return self.render_to_http_response(json_data,status=400)
#         if form.errors():
#             json_data=json.dumps({'msg':'this form conatians errors'})
#             return self.render_to_http_response(json_data,status=400)

# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#     def get_object_by_id(self,request,pk):
#         try:
#             emp=Emp.objects.get(id=pk)
#         except Emp.DoesNotExist:
#             emp=None
# #!UPDATE    
#     #-------------------------#!UPDATE-----------------------------------
#     def put(self,request,pk):
#         emp=self.get_object_by_id(id=pk)
#         if emp is None:
#             json_data=json.dumps({'msg':'no matcehd resource available'})
#             return self.render_to_http_response(json_data,status=404)
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'please provide valid json data'})
#             return self.render_to_http_response(json_data,status=404)
#         provided_data=json.loads(data)
#         original_data={
#             'ename':'bhargav',
#             'enum':127,
#             'eadres':'NYP',
#             'esal':1000
#         }
#         original_data.update(provided_data)
#         form=EmpForm(original_data,instance=emp)
#         if form.is_valid():
#             form.save()
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'thisresource updated  successfully'})
#             return self.render_to_http_response(json_data,status=400)
#         if form.errors():
#             json_data=json.dumps({'msg':'this form conatians errors'})
#             return self.render_to_http_response(json_data,status=400)

#         json_data=json.dumps({'msg':'you provided valid data'})
#         return self.render_to_http_response(json_data,status=200)
# #! DELETE   
#         def delete(self,request,pk):
#             emp=self.get_object_by_id(id=pk)
#             if emp is None:
#                 json_data=json.dumps({'msg':'no matcehd resource available'})
#                 return self.render_to_http_response(json_data,status=404)
#             status,deleted_item=emp.delete()
#             if status == 1:
#                 json_data=json.dumps({'msg':'resource delete successfully'})
#                 return self.render_to_http_response(json_data,status)
#             json_data=json.dumps({'msg':'unable to delte try again'})
#             return self.render_to_http_response(json_data)

#SESSION  9        #!ID=NONE  ERROR
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,pk):
        try:
            emp=Emp.objects.get(id=pk)
        except Emp.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please provide valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id
            if emp is None:
                json_data=json.dumps({'msg':'the requested id is not availabale'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.Serialize([emp],)
            return self.render_to_http_response(json_data)
        qs=Emp.objects.all()
        json_data=self.Serialize(qs)
        return self.render_to_http_response(json_data)