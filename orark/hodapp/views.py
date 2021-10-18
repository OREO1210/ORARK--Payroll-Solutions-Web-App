from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        
    
    else: 
        return render(request,"login.html",{'type':"HOD"})