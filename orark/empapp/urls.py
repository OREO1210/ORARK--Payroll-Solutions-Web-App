from django.urls import path
from . import views

app_name = "empapp"

urlpatterns=[
    path('login/',views.view_login,name='login'),
    path('home/',views.home,name='home'),
    path('leave/',views.leave,name='leave'),
]