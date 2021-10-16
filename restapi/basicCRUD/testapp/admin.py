from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['FirstName',
                  'LastName',
                  'MobileNumber',
                  'Email',
                  'adress']
admin.site.register(Employee,EmployeeAdmin)