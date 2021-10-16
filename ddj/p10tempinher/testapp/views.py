from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render (request,'testapp/home.html')
def movies_view(request):
    return render (request,'testapp/movies.html')
def news_view(request):
    return render (request,'testapp/news.html')
def sports_view(request):
    return render (request,'testapp/sports.html')

