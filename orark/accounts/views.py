from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request, 'landing.html')

def view_logout(request):
    logout(request)
    return redirect('/')


