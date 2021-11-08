from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from leavemangement.models import *
from itertools import chain
from datetime import datetime
from attendence.models import *


def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_receptionist:
                    login(request,user)
                    return redirect('/recep/attend')
                
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"Receptionist",'typ':'recep'})



def attd_entry(request):
    if request.method =='POST':
        att= Attendence()
        att.today_date = request.POST.get('tdate')
        att.entry_time = request.POST.get('entme')
        att.exit_time = request.POST.get('extme')
        e_l=request.POST.get('mail')
        x=User.objects.get(email=e_l)
        att.emaill = x
        y = Employees.objects.get(user=x)
        FMT='%H:%M'
        t1=att.exit_time
        t2=att.entry_time
        att.working_hrs= datetime.datetime.strptime(t1,FMT) - datetime.datetime.strptime(t2,FMT)
        att.emp= y
        att.deptid= y.dep
        att.save()
        return redirect( '/recep/attend/')
        
    elif request.user.is_authenticated and request.user.is_receptionist:
        x=Employees.objects.all()
        return render(request,"att_sheet.html",{'stu':x})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Receptionist",'typ':'recep'})

