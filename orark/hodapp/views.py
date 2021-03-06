from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from leavemangement.models import *
from itertools import chain
from datetime import date

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_hod:
                    login(request,user)
                    return redirect('/hod/profile')
                
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"HOD",'typ':'hod'})


def hodpro(request):
    if request.user.is_authenticated and request.user.is_hod:

        x=Dept.objects.get(user=request.user)
        y=Employees.objects.filter(dep=x)
        stud = LeaveRequests.objects.all().filter(dep=x)
        z=0
        for m in stud:
            if m.statuses==0:
                z += 1
        
        return render(request,'hodprofile.html',{'empp':x,'cnt':y,'pnd':z})
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
