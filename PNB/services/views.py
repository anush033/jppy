from django.shortcuts import render
def serviceview(r):
    return render(r,'services/services.html')
# Create your views here.
def cardsview(r):
    return render(r,'services/cardss.html')
def eserviceview(r):
    return render(r,'services/eservices.html')