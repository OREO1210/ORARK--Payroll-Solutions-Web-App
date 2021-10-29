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

def leave(request):
    if request.method =='POST':
        lrq=LeaveRequests()
        empl=Employees.objects.get(pk=request.user)
        depp=Dept.objects.get(pk=empl.dep)
        lrq.emp=empl
        lrq.dep=depp
        lrq.leave_sdate=request.POST.get('sdate')
        lrq.leave_edate=request.POST.get('edate')
        lrq.leave_type=request.POST.get('ltype')
        lrq.applications=request.POST.get('applications')
        lrq.statuses=0
        lrq.lop=0
        lrq.date_of_application=datetime.today()
        lrq.save()
        
    elif request.user.is_authenticated and request.user.is_employee:
        return render(request,"eleave.html",{'date':datetime.today().strftime('%Y-%m-%d')})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})

def viewleave(request):    
    if request.user.is_authenticated and request.user.is_employee:
        return render(request,"eleave.html",{'stu':final})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})
        
    