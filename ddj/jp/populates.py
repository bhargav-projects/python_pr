import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djproject.settings')
import django
django.setup

from testapp.models import *
from faker import Faker
from random import *

fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i  in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_elements(elements=('project manager','team lead','sftwr engineer'))
        feligibility=fake.random_elements(elements=('B tech','m tech','10th','12'))
        fadress=fake.adress()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,adress=fadress,email=femail,phonenumber=phonenumbergen)

populate(20)      


