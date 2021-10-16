from django.db import models

# Create your models here.
class Emp(models.Model):
    ename=models.CharField(max_length=20)
    enum= models.IntegerField()
    eadres=models.CharField(max_length=20)
    esal= models.IntegerField()