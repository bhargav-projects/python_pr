
from django.shortcuts import render

# Create your views here.
#by using cookies 
# def  Count_View(request):
#     count=int(request.COOKIES.get('count',0))
#     newcount=count+1
#     response=render(request,'testapp/cookie.html',{'count':newcount})
#     response.set_cookie('count',newcount)
#     return response

#by using session    we must migrate then runserver
def Count_View(request):
    count=int(request.session.get('count',0)) #for getting count value from page
    newcount=count+1  #incrementing evry time and storing to newcoun
    request.session['count']=newcount #storing into session obj
    print(request.session.get_expiry_age())  #set age
    print(request.session.get_expiry_date())  #set date
    response=render(request,'testapp/cookie.html',{'count':newcount})
    return response