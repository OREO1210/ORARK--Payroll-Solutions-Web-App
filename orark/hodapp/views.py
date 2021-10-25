from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from accounts.models import User,Employees

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
        messages.error(request,"Login to visit your dashboard")
    return render(request,"login.html",{'type':"HOD",'typ':'hod'})