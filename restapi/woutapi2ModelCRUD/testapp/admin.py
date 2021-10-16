from django.contrib import admin

from .models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display =['ename','enum','eadres','esal']
    
admin.site.register(Emp,EmpAdmin)