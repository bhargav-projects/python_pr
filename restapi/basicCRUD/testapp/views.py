from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.

#create
#! Retrieve
def retrieve_view(request):
    Emp_data =Employee.objects.all
    return render(request,'testapp/retrieve.html',{'Emp_data':Emp_data})

#! Create 
def create_view(request):
    form=EmployeeForm()
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')        
    return render(request,'testapp/create.html',{'form':form})

#! UPDate

def update_view(request,id):
    Emp_data =Employee.objects.get(id=id)
    if request.method == 'POST':
        form=EmployeeForm(request.POST,instance=Emp_data)
        if form.is_valid():
            form.save()
            return redirect('/')   
    return render(request,'testapp/update.html',{'Emp_data':Emp_data})     

#!  Delete
def delete_view(request,id):
    Emp_data=Employee.objects.get(id=id)
    Emp_data.delete()
    return redirect('/')