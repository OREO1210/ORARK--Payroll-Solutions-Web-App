from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.

def index(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, '../templates/login.html')

