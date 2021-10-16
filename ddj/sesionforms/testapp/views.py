from os import name
from django.http import response
from django.shortcuts import render
from .forms import NameForm,AgeForm,GfForm


# Create your views here.
def Name_view(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})
def Age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form})

def Gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=GfForm()
    return render(request,'testapp/gf.html',{'form':form})
def Results_view(request):
    gf=request.get['gf']
    request.session['gf']=gf
    return  render(request,'testapp/results.html',{'form':form})