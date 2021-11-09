from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from datetime import date, timedelta, datetime
from django.contrib.messages import get_messages
import calendar
from django.core.exceptions import ObjectDoesNotExist

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_employee:
                    login(request,user)
                    return redirect('/emp/profile')
                
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"Employee",'typ':'emp'})





def paym(request):
    if request.user.is_authenticated and request.user.is_employee:
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        return render(request,"salcur.html",{'m':currentMonth,'y':currentYear})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})


def paysl(request):
    if request.method=='POST':
        m= request.POST.get('m')
        k =Employees.objects.get( user_id = request.user.id)
        yr= m[:4]
        mon= m[-2:]
        try:
            payy= MonthlySalary.objects.get(emp = k,year=int(yr),month=int(mon))
        except ObjectDoesNotExist:
            payy = None
        if payy is not None :
            moth= calendar.month_name[int(mon)]
            return render(request,"pay.html",{ 'p':payy,'k':k,'moth':moth})
        else :
            return render(request,"noslip.html")
        
    elif request.user.is_authenticated and request.user.is_employee:
        currentMonth = datetime.datetime.now().month
        currentYear = datetime.datetime.now().year
        return render(request,"salcur.html",{'m':currentMonth,'y':currentYear})

    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'}) 


def emppro(request):
    if request.user.is_authenticated and request.user.is_employee:

        x=Employees.objects.get(user=request.user)
        
        
        return render(request,"empprofile.html",{'empp':x})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})
