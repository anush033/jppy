from django.shortcuts import render
from django.http import HttpResponse
from .models import ZaraModel
from .forms import ZaraForms


def zaracasualwear(r):
    msg = {
        'Lobbyone': 'menswear',
        'Lobbytwo': 'womenswear'
    }

    return render(r, 'cloth/clothing.html', context=msg)


# Create your views here.
def prd_details(r):
    product_list = ZaraModel.objects.all()  # ORM
    prd = {"product_list": product_list}
    return render(r, 'product/prd_list.html', context=prd)


def zaraform(r):
    form= ZaraForms()

    if r.method=='POST':
        form=ZaraForms(r.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse('<h> form is submitted</h>')
    return render(r, 'product/zaraforms.html', {'form':form})
