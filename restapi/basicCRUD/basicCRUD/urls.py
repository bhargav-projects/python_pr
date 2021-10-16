
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.retrieve_view),
        path('create/', views.create_view),
        path('update/<int:id>', views.update_view),
        path('delete/<int:id>', views.delete_view),


    
]
