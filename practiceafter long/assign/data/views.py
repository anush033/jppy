from django.shortcuts import render
from django.http import HttpResponse
from .models import datatable
from .FORMS import formdata
def datta(r):
    data_list=datatable.objects.all()
    return render(r,'data/data.html',{'data_list':data_list})
def dataf(r):
    form = formdata()

    if r.method=='POST':
        form = formdata(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>form submitted</h1>')


    return render(r,'data/forms.html',{'form':form})
# Create your views here.
