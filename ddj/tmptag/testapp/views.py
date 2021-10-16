from django.shortcuts import render
import datetime



# Create your views here.
def tags (request):
    date=datetime.datetime.now()
    name='radha krishna'
    h=int(date.strftime('%H'))
    if h<12:
        msg='hi gd mrng'
    elif h<14:
        msg=' hi gd afnn'
    else:
        msg='gd nt'

    my_dict={'date':date,'guest':name,'msg':msg}
    return render(request,('tags/hi.html'),context=my_dict)
