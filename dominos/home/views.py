from django.shortcuts import render

# Create yovur views here.
def homeview(r):
    return render(r, 'home/index.html')