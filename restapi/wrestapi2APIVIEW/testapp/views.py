from django.shortcuts import render

from rest_framework.response import Response

from testapp.serializers import NameSerializer
# Create your views here.

from rest_framework.views import APIView
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        colors=['RED','GREEN','YELLOW']
        return Response({'msg':'happy learning rest framework','colors':colors})
    def post(self, request, *args, **kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hello {} very happy to see you here '.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'hi this is put method'})
    
    def patch(self,request,*args,**kwargs):
        return Response({'msg':'hi this is patch method'})
    
    def delete(self,request,*args,**kwargs):
        return Response({'msg':'hi this is delete method'})
    
    
from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request):
        colors=['RED','GREEN','YELLOW']
        return Response({'msg':'happy new year','colors':colors})
    
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hello {} very happy to see you in testViewset '.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    
    def retrieve(self,request,pk=None):
        return Response({'msg':'hi this is retrieve  method of viewset'})
    
    def update(self,request,pk=None):
        return Response({'msg':'hi this is update  method of viewset'})
    
    def partial_update(self,request,pk=None):
        return Response({'msg':'hi this is partial_update  method of viewset'})
    
    def destroy(self,request,pk=None):
        return Response({'msg':'hi this is destroy  method of viewset'})