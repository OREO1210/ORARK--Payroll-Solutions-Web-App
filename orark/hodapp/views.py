from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from itertools import chain
from datetime import date

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_hod:
                    login(request,user)
                    return redirect('/hod/home')
                
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"HOD",'typ':'hod'})



def home(request):
    if request.user.is_authenticated and request.user.is_hod:
        return render(request,"hhome.html")
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})


def userinfo(request):
    if request.user.is_authenticated and request.user.is_hod:
        k = Dept.objects.get( user_id= request.user.id )
        stud = Employees.objects.all().filter(dep=k)
        final=[]
        for x in stud:
            l=[]
            l=[x.user.images,x.user.first_name+" "+x.user.last_name, x.user.email,x.contact,x.hire_date,x.desg.desgname]
            final.append(l)
            
        print("output", final)
        return render(request,'emptable.html',{'stu': final})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})


def leaveinfo(request):
    if request.user.is_authenticated and request.user.is_hod:            
        k = Dept.objects.get(user_id= request.user.id)
        stud = LeaveRequests.objects.all().filter(dep=k)
        pending=[]
        approved=[]
        rejected=[]
        for x in stud:
            if x.statuses==0:
                l=[]
                delta=x.leave_edate-x.leave_sdate
                print(delta.days)
                l=[x.req_id,
                   x.emp.user.first_name,
                   x.emp.user.last_name,
                   x.emp.user.email,
                   x.emp.desg.desgname,
                   x.applications,
                   x.date_of_application,
                   x.leave_sdate,
                   x.leave_edate,
                   x.leave_type,
                   delta.days]
                pending.append(l)
            elif x.statuses==1:
                l=[]
                delta=x.leave_edate-x.leave_sdate
                l=[x.req_id,x.emp.user.first_name,x.emp.user.last_name,x.emp.user.email,x.emp.desg.desgname,x.applications,x.date_of_application,x.leave_sdate,x.leave_edate,x.leave_type,x.lop,delta.days]
                approved.append(l)
            else:
                l=[]
                delta=x.leave_edate-x.leave_sdate
                l=[x.req_id,x.emp.user.first_name,x.emp.user.last_name,x.emp.user.email,x.emp.desg.desgname,x.applications,x.date_of_application,x.leave_sdate,x.leave_edate,x.leave_type,delta.days]
                rejected.append(l)
        return render(request,'hleave.html',{'pen': pending,'app':approved,'rej':rejected})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})


def leaveprocess(request, x):
    if request.user.is_authenticated and request.user.is_hod:
        if request.method == 'POST':
            lrq = LeaveRequests.objects.get(req_id=x)
            radi=request.POST.get('optionsRadios')
            if radi=="appn":
                lrq.statuses = 1
                lrq.lop = False
            elif radi=="appl":
                lrq.statuses = 1
                lrq.lop = True
            else:
                lrq.statuses=2
                lrq.lop = False
            lrq.save()
            
        return redirect("/hod/leave")
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})

