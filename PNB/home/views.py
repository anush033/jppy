from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect


def homeview(r):
    return render(r, 'home/index.html')


# Create your views here.
def signupview(r):
    form = SignupForm()
    if r.method == 'POST':
        form = SignupForm(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/acountdetails")

    return render(r, 'home/signup.html', {'form': form})
