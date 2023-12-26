from django.shortcuts import render
from django.http import HttpResponse
from .models import beveModel


# Create your views here.

def beverages_show(r):
    beve_list=beveModel.objects.all()
    obj={'beve_list':beve_list}
    return render(r,'beverages/beve.html',context=obj)
