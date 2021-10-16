from django.shortcuts import render
from testapp.models import Emp
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'testapp/index.html')
def home(request):
    emp_list=Emp.objects.all()
    my_dict={'emp_list':emp_list}
    return render (request,'testapp/hai.html',context=my_dict)

