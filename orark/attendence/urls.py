from django.urls import path
from . import views

app_name = "attendence"

urlpatterns=[
    path('login/',views.view_login,name='login'),
    path('attend/',views.attd_entry,name='attend')
]