
from django.shortcuts import render,redirect
from .models import StudentModel
from .forms import StudentForm,StudentForm2
# # Create your views here.

def Home_view(request):
    return render(request,'StudentApp/home.html')

def New_Student_View(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'StudentApp/register.html',{'form':form})


def Find_Student_View(request):
    
    Student_details=StudentModel.objects.all()
    form =StudentForm2(request.POST or None)
    context={'Student_details':Student_details,'form':form}
    if request.method == 'POST':
        Student_details=StudentModel.objects.all().filter(Roll_Number__pk=form['Roll_Number'].value())
    return render(request,'StudentApp/Find_details.html',context)


# def Find_Student_View(request):
#     # if request.method == 'GET':
#     #     form=StudentForm2()
#     #     return render(request,'StudentApp/Find_details.html',{'form':form})
#     if 'q' in request.GET:
#         q=request.GET['q']
#         Student_details=StudentModel.objects.filter(Roll_Number__contins=q)
#     # else:
#     #     Student_details=StudentModel.objects.all()
#         return render(request,'StudentApp/Find_details.html',{'Student_details':Student_details})


# def Find_Student_View(request):
#     if 'q' in request.POST:
#         query=request.GET('q')
#         return StudentModel.objects.all()
#     else:
# #         Student_details=StudentModel.objects.filter(Roll_Number__contins=q)
# #     # else:
#         Student_details=StudentModel.objects.all()
#         return render(request,'StudentApp/Find_details.html',{'Student_details':Student_details})

