 
from django.contrib import admin
from django.urls import path,include
from StudentApp import views
 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home_view),
    path('New_Student/', views.New_Student_View),
    path('search/', views.Find_Student_View),
    ]
    
    
    
# <int:id>/
  # path('search/<int:Roll_number>/', views.Find_Student_View),