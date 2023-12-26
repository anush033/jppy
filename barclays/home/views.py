from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(r):
    return render(r,'home/index.html')

def logout(r):
    return render(r,'home/logout.html')

def signup(r):
    form = SignUpForm()
    if r.method=='POST':
        form = SignUpForm(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect("/accounts/login/")
    return render(r,'home/signupform.html',{'form':form})
