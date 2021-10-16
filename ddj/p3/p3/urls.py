
from django.contrib import admin
from django.urls import path,include
from p3app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('p3app.urls')),
]
    
