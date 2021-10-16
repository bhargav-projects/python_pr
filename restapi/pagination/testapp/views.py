from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView


#?for gloabal pagination rules 
# class StudentListView(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

'''customised pagination rules 
#we can define custom pagination for particular view
#only thing u need to import and use that class in views .py 
'''
from .mypagination import MyPageNumberPagination
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination




#DJANGO BASED PAGINATION ------------------------
post_list=post.objects.all()
#it shows number of (reocrds)posts per page 
paginator=Paginator(post_list,3)
#it  get page number 
page_number=paginator.GET.get('page')

try:
    #if user used page attributes 
    post_list=paginator.page(page_number)
    #if user dont use page attributes we get error so handle and we will provide first page
except PageNotAnInteger:
    post_list=paginator.page('1')
    #if user wants last page if he clicks we dont show empty page 
    #we will display last page if he reches last page
except Emptypage:
    post_list=paginator.page(paginator.Num_pagese)