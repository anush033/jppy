from django.shortcuts import render
from django.http import HttpRequest


def zarafootwearmen(r):
    msg1={'VarietyA':'flip_flops',
        'VarietyB':'sports_shoes',
        'VarietyC':'sneakers'
        }
    return render(r,'footwear/footwear.html',context=msg1)
def zaradetail(r):
    return render(r,'footwear/index.html')

# Create your views here.
