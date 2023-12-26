from django.shortcuts import render

# Create your views here.
def indexView(r):
    return render(r,'home/index.html')