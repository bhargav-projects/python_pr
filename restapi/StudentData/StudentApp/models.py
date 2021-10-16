from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Roll_Number=models.IntegerField()
    First_Name=models.CharField(max_length=64)
    Second_Name=models.CharField(max_length=64)
    Age=models.IntegerField()