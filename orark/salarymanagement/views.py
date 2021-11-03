from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from itertools import chain
from datetime import date

# Create your views here.

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_superuser:
                    login(request,user)
                    return render(request,"saldet.html",{'type':"AD",'typ':'ad'})
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"AD",'typ':'ad'})



def home(request):
    return render(request,"adhome.html",{'type':"AD",'typ':'ad'})

def saladett(request):
    if request.method =='POST':
        cea =request.POST.get('cea')
        hra=request.POST.get('hra')
        ma=request.POST.get('ma')
        ta=request.POST.get('ta')
        fda=request.POST.get('fda')
        vda=request.POST.get('vda')
        pf=request.POST.get('pf')
        b=request.POST.get('b')
        
   