from django.shortcuts import render
from formdata import forms


def student_view(request):
    form=forms.studentregister()
    if(request.method == 'POST'):
        frm=forms.studentregister(request.POST)
        if(frm.is_valid()):
            frm.save(commit=True)
            return render(request,'formdata/thank.html')

    return render(request,'formdata/register.html',{'form':form})