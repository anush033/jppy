from django.shortcuts import render
from django.http import HttpResponse
from .models import PizzaModel
from .forms import pizzafeedbackforms

# Create your views here.
def pizza_show(r):
    pizza_list = PizzaModel.objects.all()
    obj = {'pizza_list': pizza_list}
    return render(r, 'pizza/pizza.html', context=obj)
def formpizza(r):
    objj=pizzafeedbackforms()
    md={'objj':objj}
    return render(r,'pizza/formfeedback.html',context=md)

def pizzaveg(r):
    return render(r, 'pizza/pizzaveg.html')