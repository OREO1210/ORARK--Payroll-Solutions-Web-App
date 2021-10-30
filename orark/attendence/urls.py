from django.urls import path
from . import views

app_name = "attendence"

urlpatterns=[
    path('login/',views.view_login,name='login'),
    path('home/',views.home,name='home'),
    path('attend/',views.attd_entry,name='attend')
]