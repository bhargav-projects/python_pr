from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    MobileNumber = models.IntegerField()
    Email = models.EmailField()
    adress=models.TextField(max_length=200)
    