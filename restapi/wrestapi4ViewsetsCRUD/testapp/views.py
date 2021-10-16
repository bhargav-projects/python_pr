from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from testapp.permissions import IsReadOnly,IsGetOrPatch
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 
# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    #!-----------authentication-------------!#
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    # permission_classes=[IsReadOnly,IsGetOrPatch,TracarPermission]

    