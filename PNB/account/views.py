from django.shortcuts import render
from .models import FormsfieldsModel
from .forms import AccountOpeningForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def savingsview(r):
    return render(r, 'account/forms.html')


# Create your views here.
@login_required
def accountopeningdetail(r):
    accounts = FormsfieldsModel.objects.all()
    return render(r, 'account/accountdetails.html', {'accounts': accounts})

def submitted(r):
    return render(r,'account/submitt.html')

def openingviews(r):
    obj = AccountOpeningForm()
    if r.method == 'POST':
        obj = AccountOpeningForm(r.POST)
        if obj.is_valid():
            obj.save()
            return HttpResponseRedirect('/accounts/formssubmitted/')
        return render(r, 'account/forms.html', {'obj': obj})
def logout(r):
    return render(r,"home/logout.html")
def delete(r,id):
    record=FormsfieldsModel.objects.get(acc_id=id)
    record.delete()
    return HttpResponseRedirect("/accounts/acountdetails/")
def update(r,id):
    record=FormsfieldsModel.objects.get(acc_id=id)
    if r.method == 'POST':
        form = AccountOpeningForm(r.POST,instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/acountdetails/')
    return render(r,'account/update.html',{'record':record})

