from django.urls import path
from . import views

app_name = "hodapp"

urlpatterns=[
    path('login/',views.view_login,name='login'),
    path('home/',views.home,name='home'),
]