from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_view(request):
    return render(request,'testapp/jav.html')


def logout_view(request):
    return render(request,'testapp/logout.html')


def signup_view(request):
    form=forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})