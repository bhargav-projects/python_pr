
from django.contrib import admin
from django.urls import path
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_view),
    path('addmovie/',views.add_Movies_view),
    path('listmovies/',views.list_movies),
]
