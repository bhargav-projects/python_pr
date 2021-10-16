from django import forms
from django.core.exceptions import ValidationError
from django.core import validators



def sat(value):
    if value [0] !=b:
        raise  forms.ValidationError('name starts with b')


class feedback(forms.Form):
    name=forms.CharField(validators=[sat])
    marks=forms.IntegerField()
    email=forms.CharField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    

def clean_name(self):
    inputname= self.cleaned_data["name"]
    if inputname <4 :
        raise validators('wrong')
    return inputname

        