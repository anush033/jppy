from django.shortcuts import render
from .models import PersonalDetailsModel
from .forms import EmpDetailsForms


# Create your views here.
def loan_details(r):
    return render(r, 'loan/loaninfo.html')

def emp_details(r):
    emp_list=PersonalDetailsModel.objects.all() #ORM
    emp = {"emp_list":emp_list}
    return render(r,'employee/emplist.html',context=emp)


def empform(r):
    obj= EmpDetailsForms()
    md={"obj":obj}
    return render(r,'employee/empform.html',context=md)
