from django.db import models

# Create your models here.

class Emp (models.Model):
    ename=models.CharField( max_length=50)
    enum=models.IntegerField()
    esal=models.IntegerField()
    eadr=models.CharField(max_length=50)


    def __str__(self):
        return self.ename
