from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'templates/testapp/index.html')

def sportsinfo(request):
    return render (request,'templates/testapp/news.html')

def moviesinfo(request):
    head_msg='latest movies info'
    msg1='hi 1st news'
    msg2='hi 2st news'
    msg3='hi 3st news'

    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render (request,'templates/testapp/news.html',context=my_dict)

def politicsinfo(request):
    return render (request,'templates/testapp/news.html')