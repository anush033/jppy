from django.shortcuts import render
from .models import AccountOpeningModel
from .forms import AccountOpeningForm
from django.http import HttpResponseRedirect


# Create your views here.


def savingView(r):
    return render(r, 'accounts/saving.html')


def currentView(r):
    return render(r, 'accounts/current.html')


def traddingView(r):
    return render(r, 'accounts/tradding.html')


def accountopeningdetails(r):
    accounts = AccountOpeningModel.objects.all()
    return render(r, 'accounts/accountsdetails.html', {'accounts': accounts})


def openingviews(r):
    form = AccountOpeningForm()
    if r.method == 'POST':
        form = AccountOpeningForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/accountdetails/')

    return render(r, 'accounts/openingform.html', {'form': form})
