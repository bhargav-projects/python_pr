from django.contrib import admin
from testapp.models import Emp

    


class EmpAdmin(admin.ModelAdmin):
    list_display=['id','ename','enum','eadr','esal']
    

admin.site.register(Emp,EmpAdmin)