from django.urls import path
from . import views

app_name = "leavemangement"

urlpatterns=[
    path('hod/',views.hodleaveinfo,name='leave'),
    path('hod/<int:x>',views.hodleaveprocess,name='requestprocessing'),
    path('emp/',views.empleave,name='leave1'),
    path('empviewleave/',views.empviewleave,name='leave2'),
]