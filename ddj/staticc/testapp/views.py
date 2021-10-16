from django.shortcuts import render




# Create your views here.

def home (request):
    return render(request,'testapp/guest.html')
def hi(request):
    return render(request,'testapp/hi.html')
    