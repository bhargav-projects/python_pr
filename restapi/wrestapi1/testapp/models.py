from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=30)
    enum=models.IntegerField()
    esal=models.IntegerField()
    eadres=models.CharField(max_length=30)
        