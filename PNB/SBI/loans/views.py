from django.shortcuts import render
from .models import LoandetailsModel
from .forms import Loanform
from django.http import HttpResponseRedirect
# Create your views here.
def loanview(r):
    return render(r,'loans/loaninfo.html')
def emp_details(r):
    emp_list=LoandetailsModel.objects.all()
    emp={'emp_list':emp_list}
    return render(r,'loans/emplist.html',context=emp)
def formviews(r):
    obj = Loanform()
    if r.method == 'POST':
        obj = Loanform(r.POST)
        if obj.is_valid():
            obj.save()
            return HttpResponseRedirect('loans/empdetails/')
        return render(r, 'loans/loanforms.html', {'obj': obj})
