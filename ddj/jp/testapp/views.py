from django.shortcuts import render
from testapp.models import hydjobs
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hyd.html',context=my_dict)