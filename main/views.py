from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    username = 'Siri'
    # return HttpResponse("<h2>Hello, This is working!</h2>")
    return render(request,'index.html',{'name':username})


def aboutus(request):
        
    return render(request,'aboutus.html')


def login(request):
    return render(request,'login.html')
