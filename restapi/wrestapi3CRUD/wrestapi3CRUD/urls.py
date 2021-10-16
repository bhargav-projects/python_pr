 
from django.contrib import admin
from django.urls import path
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',views.EmployeeListAPIView.as_view()),
    # path('api/',views.EmployeeCreateAPIView.as_view()),
    # path('api/<int:pk>/',views.EmployeeRetrieveAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeUpdateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeDestroyAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveUpdateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveDestroyAPIView.as_view()),
    
    # #! THESE 2 ENOUGH FOR  ALL CRUD OPERATIONS
    # path('api/',views.EmployeeListCreateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),

    path('api/',views.EmployeeListCreateModelMixin.as_view()),
    path('api/<int:id>/',views.EmployeeRetrieveUpdateDestroyModelMixin.as_view()),





]
