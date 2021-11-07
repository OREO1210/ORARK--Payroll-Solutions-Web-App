from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from datetime import datetime

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_employee:
                    login(request,user)
                    return redirect('/emp/home')
                
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"Employee",'typ':'emp'})



def home(request):
    if request.user.is_authenticated and request.user.is_employee:
        return render(request,"ehome.html")
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})

        
    

def paysl(request):
    if request.user.is_authenticated and request.user.is_employee:
        k =Employees.objects.get( user_id = request.user.id )
        payy= MonthlySalary.objects.all()
        print("output------------------------------------", k.emp_id)
        return render(request,"pay.html")
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'}) 
