from django.forms import ModelForm
from StudentApp.models import StudentModel

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields ='__all__'
        
class StudentForm2(ModelForm):
    class Meta:
        model = StudentModel
        fields =['Roll_Number',]

