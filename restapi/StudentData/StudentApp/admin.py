from django.contrib import admin
from .models import StudentModel
# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['Roll_Number','First_Name','Second_Name','Age']
admin.site.register(StudentModel,StudentModelAdmin)