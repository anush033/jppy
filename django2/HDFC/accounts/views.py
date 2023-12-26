from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def account_details(r):
    acc_dict={'emp_id':164694646,
        'account number':16514694949,
        'account_type':'saving account',
        'loan bal':156161691,
        'tenure':4
    }

    return render(r,"accounts/accountinfo.html",context=acc_dict)
