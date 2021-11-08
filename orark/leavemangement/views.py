from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from leavemangement.models import *
from itertools import chain
from datetime import datetime

# Create your views here.

def hodleaveinfo(request):
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
                approved.append(l)
            else:
                l=[]
                delta=x.leave_edate-x.leave_sdate
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
                rejected.append(l)
        return render(request,'hleave.html',{'pen': pending,'app':approved,'rej':rejected})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})


def hodleaveprocess(request, x):
    if request.user.is_authenticated and request.user.is_hod:
        if request.method == 'POST':
            lrq = LeaveRequests.objects.get(req_id=x)
            radi=request.POST.get('optionsRadios')
            if radi=="appn":
                lrq.statuses = 1
            else:
                lrq.statuses = 2
            lrq.save()
        return redirect('/leave/hod' )
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})

def empleave(request):
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
        lrq.date_of_application=datetime.today()
        lrq.save()
        return redirect("/leave/emp")
        
    elif request.user.is_authenticated and request.user.is_employee:
        return render(request,"eleave.html",{'date':datetime.today().strftime('%Y-%m-%d')})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})

def empviewleave(request):    
    if request.user.is_authenticated and request.user.is_employee:
        k = Employees.objects.get(user=request.user.id)
        stud = LeaveRequests.objects.all().filter(emp=k)
        final=[]
        for x in stud:
            l=[]
            delta=x.leave_edate-x.leave_sdate
            l=[x.req_id,
               x.applications,
               x.date_of_application,
               x.leave_sdate,
               x.leave_edate,
               x.leave_type,
               delta.days,
               x.statuses]
            final.append(l)
        return render(request,"eleaveview.html",{'stu':final})
    else:
        messages.error(request,"Please Login to continue")
    return render(request,"login.html",{'type':"Employee",'typ':'emp'})
