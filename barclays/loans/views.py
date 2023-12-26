from django.shortcuts import render
from .models import LoanDetailsModel
from .forms import LoanDetailsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def LoanFormViews(r):
    form = LoanDetailsForm()

    if r.method=='POST':
        form = LoanDetailsForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/loans/loandetails/")

    return render(r,'loans/loanform.html',{'form':form})


@login_required
def LoanDetailsViews(r):
    #loan_objects = LoanDetailsModel.objects.all()
    loan_objects = LoanDetailsModel.objects.filter(age__lte=25)
    loan_objects = LoanDetailsModel.objects.filter(city__exact='mumbai')
    loan_objects = LoanDetailsModel.objects.filter(city__exact='mumbai')
    loan_objects = LoanDetailsModel.objects.filter(name__contains='O')
    loan_objects = LoanDetailsModel.objects.filter(name__icontains='O')
    loan_objects = LoanDetailsModel.objects.filter(loanid__in=[546,541])
    loan_objects = LoanDetailsModel.objects.filter(name__startswith='s')
    loan_objects = LoanDetailsModel.objects.filter(name__endswith='m')

    loan_objects = LoanDetailsModel.objects.filter(name__startswith='s') & LoanDetailsModel.objects.filter(age__lt=25)
    loan_objects = LoanDetailsModel.objects.exclude(name__startswith='O')
    loan_objects = LoanDetailsModel.objects.all().order_by('-age')
    print(loan_objects)

    return render(r,'loans/loandetails.html',{'loan_objects':loan_objects})


def delete(r,id):
    record = LoanDetailsModel.objects.get(loanid=id)
    record.delete()
    return HttpResponseRedirect("/loans/loandetails/")

def update(r,id):
    record = LoanDetailsModel.objects.get(loanid=id)
    if r.method == 'POST':
        form = LoanDetailsForm(r.POST,instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/loans/loandetails/")


    return render(r,'loans/update.html',{'record':record})