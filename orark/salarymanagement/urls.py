from django.urls import path
from . import views

app_name = "salarymanagement"

urlpatterns=[
    path('home/',views.home,name='adhome'),
    path('login/',views.view_login,name='adlogin'),   
]