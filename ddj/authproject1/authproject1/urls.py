

from django.contrib import admin
from django.conf.urls import url,include
from testapp import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url('',views.home_view),
    url('java/',views.java_view),
    url('accounts/',include('django.contrib.auth.urls')),
    url('logout/',views.logout_view),     
    url('signup/',views.signup_view),
     
]
