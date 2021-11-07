from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import *
from itertools import chain
from datetime import date, timedelta, datetime
from attendence.models import *
from leavemangement.models import *
import calendar

# Create your views here.

def view_login(request):
    if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_superuser:
                    login(request,user)
                    return redirect('/ad/addhome')
            else:
                messages.error(request,"Invalid email or password")

    return render(request,"login.html",{'type':"AD",'typ':'ad'})



def home(request):
    return render(request,"adhome.html",{'type':"AD",'typ':'ad'})

def addhome(request):
    return render(request,"saldet.html")

def saladett(request):
    if request.method =='POST':
        cea =request.POST.get('cea')
        hra=request.POST.get('hra')
        ma=request.POST.get('ma')
        ta=request.POST.get('ta')
        fda=request.POST.get('fda')
        pf=request.POST.get('pf')
        b=request.POST.get('b')
        maxleave=request.POST.get('maxleave')
        months=request.POST.get('month')
        maxhours=request.POST.get('maxhours')
        
        usrlist=Employees.objects.all()
        alldays=days_cur_month(months)
        
        for usr in usrlist:  
        # Attendance processing
            atx = Attendence.objects.filter(emp=usr)
            appl = LeaveRequests.objects.filter(emp=usr, statuses=1)
            appldays = []
            attx=[]
            for x in appl:
                sdate = datetime.datetime.strptime(str(x.leave_sdate),'%Y-%m-%d')
                edate = datetime.datetime.strptime(str(x.leave_edate),'%Y-%m-%d')
                y = [(sdate + timedelta(days=x)).strftime('%Y-%m-%d') for x in range((edate-sdate).days)]
                appldays.append(edate)
                appldays.append(y)
            for x in atx:
                sdate = str(x.today_date)
                attx.append(sdate)
            workingdays=0
            absentdays=0
            paydays=0
            for x in alldays:
                if x in attx:
                    workingdays += 1
                    paydays += 1
                elif x in appldays:
                    absentdays += 1
                else:
                    absentdays += 1
            paydays += min(len(appldays),int(maxleave))
        # Attendance processing ends
        # Overtime processing
            whrs = Attendence.objects.filter(emp_id=usr).values_list('working_hrs')
            othours=0
            for w in whrs:
                z=str(w)[2:-3]
                t1=datetime.datetime.strptime(maxhours,"%H:%M")
                t2=datetime.datetime.strptime(z,"%H:%M:%S")
                
                ot=t1-t2
                ox=str(ot)
                if ox[0] != '-':
                    othours += int(ox[0])
        # Overtime processing ends
            basic = (usr.desg.amount)*(paydays)
            da = ((float(fda)*basic)/100)
            bbda = basic + da
            tral = (float(ta)/100)*(bbda)
            ceal = float(cea) * min(2,usr.no_of_children)
            hral = (float(hra)/100)*(bbda)
            mall = (float(ma)/100)*(bbda)
            pfnd = (float(pf)/100)*(bbda)
            bons = float(b)
        
            slab = SlabTable.objects.all()
            escc=0
            itxx=0
            ptxx=0
            for xx in slab:
                if bbda > xx.llim and bbda < xx.ulim:
                    escc = (xx.esic/100)*bbda
                    itxx = (xx.itax/100)*bbda
                    ptxx = xx.ptax
                    break
                
            otpp=((usr.desg.amount)/(int(maxhours[:2]))) * othours
            
            totl=bbda+tral+ceal+hral+mall+bons+otpp-pfnd-escc-itxx-ptxx
            
            msl = MonthlySalary()
            msl.emp=usr
            msl.year=int(months[:4])
            msl.month=int(months[-2:])
            msl.workingdays=workingdays
            msl.absentdays=absentdays
            msl.paydays=paydays
            msl.basic=basic
            msl.othr=othours
            msl.otpay=otpp
            msl.da=da
            msl.pf=pfnd
            msl.esic=escc
            msl.itax=itxx
            msl.ptax=ptxx
            msl.bonus=bons
            msl.ma=mall
            msl.ta=tral
            msl.hra=hral
            msl.cea=ceal
            msl.total=totl
            
            msl.save()
        
        # LeaveRequests.objects.all().delete()
        # Attendence.objects.all().delete()

        

    
 
def days_cur_month(months):
    m = int(months[-2:])
    y = int(months[:4])
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
    
    
    
            
        
        
        
   