from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"p3app/home.html")
def contacts(request):
    my_dict={'msg':'hi'}
    return render(request,"p3app/contacts.html",my_dict)