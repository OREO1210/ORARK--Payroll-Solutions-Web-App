from django.urls import path
from . import views

app_name = "empapp"

urlpatterns=[
    path('login/',views.view_login,name='login'),
    path('profile/',views.emppro,name='profile'),
    path('payslip/',views.paym,name='paym'),
    path('payview/',views.paysl,name='paysl')
]