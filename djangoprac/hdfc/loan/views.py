from django.shortcuts import render
from django.http import HttpResponse
def variant(r):

    return render(r,'loan/loaninfo.html')
# Create your views here.
