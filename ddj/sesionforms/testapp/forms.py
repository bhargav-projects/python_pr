from django import forms


class NameForm(forms.Form):
    name=forms.ChoiceField()
class AgeForm(forms.Form):
    age=forms.IntegerField()
class GfForm(forms.Form):
    gf=forms.CharField()