from django.urls import path
from . import views

app_name = "empapp"

urlpatterns=[
    path('login/',views.login)
]