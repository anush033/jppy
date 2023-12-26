from django.shortcuts import render

# Create your views here.
def homeview(r):
    return render(r,'home/index.html')
