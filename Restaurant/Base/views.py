from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from Base.models import login
from Base.models import reservation
from django.contrib import auth
from django.contrib.auth import authenticate



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def menu(request):
    return render(request, 'menu.html')
    

def reservation(request):
       return render(request, 'reservation.html')



    
def login(request):
      return render(request, 'login.html')
        


 


