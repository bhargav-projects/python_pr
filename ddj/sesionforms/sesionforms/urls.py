
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Name_view),
    path('age/',views.Age_view),
    path('gf/',views.Gf_view),
    path('results/',views.Results_view),
]
