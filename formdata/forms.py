from django import forms
from django import forms
from formdata.models import student


class studentregister(forms.ModelForm):
    
    class Meta:
        model = student 
        fields = '__all__'




