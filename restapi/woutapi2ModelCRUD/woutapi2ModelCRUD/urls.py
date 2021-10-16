
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',views.EmployeeDetailCBV.as_view()),
    
    #for user want to enter id 
    #path('api/<str:pk>/',views.EmployeeDetailCBV.as_view()), 
    
    #csrf_exempt
    #path('listapi/',views.EmployeeListCBV.as_view())
    #path('api/',views.EmployeeListCBV.as_view()),
    # !update session8
    #path('api/<str:pk>/',views.EmployeeDetailCBV.as_view()), 
    #session9
    path('api/',views.EmployeeCRUDCBV.as_view()), 
]
