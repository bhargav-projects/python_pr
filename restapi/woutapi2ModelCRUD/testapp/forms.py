from django import forms 
from .models import Emp
class EmpForm(forms.ModelForm):
    def clean_esal(self):
        input_sal = self.cleaned_data['esal']
        if input_sal < 5000:
            raise forms.ValidationError('salary should be more than 5000')
        return input_sal
    class Meta:
        model = Emp
        fields ='__all__'   