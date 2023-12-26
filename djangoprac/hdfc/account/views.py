from django.shortcuts import render
def acc_details(r):
    acc_dict={'emp_id':12344565,
              'ac_no':122445676,
              'name':'ashu'
    }
    return render(r,'account/accountsinfo.html',context=acc_dict)
# Create your views here.
