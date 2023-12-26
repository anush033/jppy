from django.shortcuts import render
from django.http import HttpRequest
def employee_details(r):
    return render(r, 'dep/depinfo.html')

# Create your views here.
