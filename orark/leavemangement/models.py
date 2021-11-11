from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django import forms
from accounts.models import *
# Create your models here.

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class LeaveRequests(models.Model):
    req_id = models.AutoField(db_column='Req_id', primary_key=True)   
    emp = models.ForeignKey(Employees, models.DO_NOTHING, db_column='Emp_id')   
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')   
    leave_sdate = models.DateField(db_column='Leave_SDate')   
    leave_edate = models.DateField(db_column='Leave_EDate')   
    leave_type = models.CharField(db_column='Leave_Type', max_length=700)   
    applications = models.CharField(db_column='Applications', max_length=700, blank=True, null=True)   
    statuses = models.IntegerField(db_column='Statuses')   
    date_of_application = models.DateField(db_column='Date_of_application', blank=True, null=True)   

    class Meta:
         
        db_table = 'leave_requests'

    def __str__(self):
        return self.req_id