from django.db import models

# Create your models here.

class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    eligibility=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phoneno=models.IntegerField()
class nellorejobs(models.Model):
    date=models.DateField()
    company=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    eligibility=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phoneno=models.IntegerField()
class vmpjobs(models.Model):
    date=models.DateField();
    company=models.CharField( max_length=50);
    title=models.CharField( max_length=50);
    eligibility=models.CharField(max_length=50);
    adress=models.CharField(max_length=50);
    email=models.EmailField(max_length=254);
    phoneno=models.IntegerField()

    def __str__(self):
        return self.name
