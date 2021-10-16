
from django.contrib import admin
from testapp.models import hydjobs,nellorejobs,vmpjobs

# Register your models here.

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','adress','email','phoneno']
class nelloreAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','adress','email','phoneno']
class vmpAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','adress','email','phoneno']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(nellorejobs,nelloreAdmin)
admin.site.register(vmpjobs,vmpAdmin)