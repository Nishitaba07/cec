from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def country(request):
    return render(request,'1.html')

def India(request):
    return render(request,'India.html')

def Australia(request):
    return render(request,'Australia.html')

def America(request):
    return render(request,'America.html')

def Gujarat(request):
    return render(request,'Gujarat.html')
def Maharashtra(request):
    return render(request,'Maharashtra.html')
def Karnataka(request):
    return render(request,'Karnataka.html')

def gandhinagar(request):
    return render(request,'gandhinagar.html')

def newsouthwales(request):
    return render(request,'newsouthwales.html')

def Queensland(request):
    return render(request,'Queensland.html')


def SouthAustralia(request):
    return render(request,'SouthAustralia.html')


def Tsamnia(request):
    return render(request,'Tsamnia.html')





