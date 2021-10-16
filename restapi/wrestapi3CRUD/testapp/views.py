from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

#!crud operations
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,
                                    RetrieveUpdateDestroyAPIView
                                     )


from testapp.serializers import EmployeeSerializer
'''#?               THESE 2 ENOUGH FOR ALL CRUD OPERATIONS   
    #-----------------#!listCreate OPERATION---------------------#
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 
    
    #-----------------#!RetrieveUpdateDestroy OPERATION---------------------#
class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 
    lookup_field='id'   '''
    


# class EmployeeListAPIView(APIView):
#     def get(self, request,format=None):
#         qs=Employee.objects.all()
#         #this serializer converts the query sets into python native dict format
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data) #this response converts python native data to json.

#     #-----------------#!List OPERATION---------------------#
# class EmployeeListAPIView(ListAPIView):
#     #queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
    
#     #-----------------#!SEARCH OPERATION---------------------#
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('name')
#         if name is  not None:
#             qs=qs.filter(ename__contains=name)
#         return qs
    
#     #-----------------#!Create OPERATION---------------------#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 

#     #-----------------#!Retrieve OPERATION---------------------#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
#     lookup_field='id' #if we dont use lField them change url like <int:pk>

#     #-----------------#!Update OPERATION---------------------#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
#     lookup_field='id'  
    
#     #-----------------#!Destroy OPERATION---------------------#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
#     lookup_field='id'    
    
#         #-----------------#!RetrieveUpdate OPERATION---------------------#
# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
#     lookup_field='id'   
    
#             #-----------------#!RetrieveDestroy OPERATION---------------------#
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer 
#     lookup_field='id'   



#!                     MIXINS  sessoin-18
''' 
we use these type of Mixins very rarely, 
so we don't need to focus too much'
'''

from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin
class EmployeeListCreateModelMixin(CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    
    
class EmployeeRetrieveUpdateDestroyModelMixin(UpdateModelMixin,DestroyModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request,*args,**kwargs)
    def destroy(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


#! conclusion
'''if you want to develope crud operations fastly and easy way go to viewset 
   if you want complex operations and code execution flow and control over the code then Apiview
   model mixins are just for awarness purpose and these are parent class of APIviews internally
'''