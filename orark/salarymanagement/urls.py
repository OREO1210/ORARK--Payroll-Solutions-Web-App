from django.urls import path
from . import views

app_name = "salarymanagement"

urlpatterns=[
    path('home/',views.home,name='adhome'),
    path('login/',views.view_login,name='adlogin'),
    path('addhome/',views.addhome,name='addhome'),
    path('pay/',views.saladett,name='pay'),
]