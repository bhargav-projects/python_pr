from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.



def dif(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1> hey krishna very '
    if h<12:
        msg=msg+'good morn'
    elif h<4:
        msg=msg+'good afnn'
    elif h<6:
        msg=msg+'good evn'
    elif h<8:
        msg=msg+'good nt'
    else:
        msg=msg+'its sleeping time'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1>now server time is'+str(date)+'</h1>'
    return HttpResponse(msg)


