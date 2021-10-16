from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from testapp import views

router =  DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)
        #if its model view set basename is optional
#router.register('api',views.EmployeeCRUDCBV,basename='api')
 
from rest_framework.authtoken import views
from rest_framework_jwt.view import obtaining_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-api-token',views.obtain_auth_token,name='get_api_token'),

    path('auth-jwt/',obtaining_jwt_token),
    path('auth-jwt-refresh/',refresh_jwt_token),
    path('auth-jwt-verify/',verify_jwt_token),


]
