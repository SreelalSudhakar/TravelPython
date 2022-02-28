from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Team

# Create your views here.


def index(request):
    place = Place.objects.all()
    team = Team.objects.all()
    return render(request,'index.html',{'res':place,'result':team})
    
def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

def details(request):
    return HttpResponse("Details are here !")

def thanks(request):
    return HttpResponse("Thank you all !")

def operation(request):
    no1=int(request.GET['x'])
    no2=int(request.GET['y'])
    result1 = no1+no2
    result2 = no1-no2
    result3 = no1*no2
    result4 = no1/no2
    return render(request,'contact.html',{'addition':result1,'subtraction':result2,'multiple':result3,'division':result4})    