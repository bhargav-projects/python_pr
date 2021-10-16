from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.CharField(max_length=255)
    ename=models.CharField(max_length=255)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=255, blank=True)