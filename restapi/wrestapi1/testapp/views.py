from django.shortcuts import render

from .models import Employee
from testapp.serializers import EmployeeSerializer

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serailizer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serailizer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serailizer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serailizer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        serailizer=EmployeeSerializer(data=p_data)
        if serailizer.is_valid():
            serailizer.save()
            msg={'msg':'resource posted successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serailizer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    
    def put(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id' )
        emp=Employee.objects.get(id=id)
        serailizer=EmployeeSerializer(emp,data=p_data,partial=True)
        if serailizer.is_valid():
            serailizer.save()
            msg={'msg':'resource updated successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serailizer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    def delete(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id' )
        emp=Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'resource deleted successfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')
            