
from django.shortcuts import render
from . import forms
# Create your views here.
def thankyou_view(request):
    return render(request,'testapp/tqu.html')


def feedback_view(request):
    if request.method == 'GET':
        form=forms.feedback()
        
    form=forms.feedback()
    if request.method == 'POST':
        form=forms.feedback(request.POST)
        if form.is_valid():
            print(' get students data successfully')
            print('name:',form.cleaned_data['name'])
            print('marks:',form.cleaned_data['marks'])
    return render(request,'testapp/feedback.html',{'form':form})


