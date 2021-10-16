from django.db import models
from django.db.models import Model
# Create your models here.
class Student(Model):
    name=models.CharField(max_length=50)
    #roll number should be +ve
    roll=models.PositiveIntegerField() #it wont accept negative values
    