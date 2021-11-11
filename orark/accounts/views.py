from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request, 'landing.html')

def view_logout(request):
    logout(request)
    return redirect('/')

def handle404(request,exception,template_name="error-404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handle500(request, *args, **argv):
    return render(request, 'error-500.html', status=500)

def handle400(request, *args, **argv):
    return render(request, 'error-400.html', status=500)

def handle403(request, *args, **argv):
    return render(request, 'error-403.html', status=500)
