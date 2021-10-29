from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django import forms
from accounts.models import *
# Create your models here.

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class LeaveRequests(models.Model):
    req_id = models.AutoField(db_column='Req_id', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey(Employees, models.DO_NOTHING, db_column='Emp_id')  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    leave_sdate = models.DateField(db_column='Leave_SDate')  # Field name made lowercase.
    leave_edate = models.DateField(db_column='Leave_EDate')  # Field name made lowercase.
    leave_type = models.CharField(db_column='Leave_Type', max_length=700)  # Field name made lowercase.
    applications = models.CharField(db_column='Applications', max_length=700, blank=True, null=True)  # Field name made lowercase.
    statuses = models.IntegerField(db_column='Statuses')  # Field name made lowercase.
    lop = models.BooleanField(db_column='LOP')  # Field name made lowercase.
    date_of_application = models.DateField(db_column='Date_of_application', blank=True, null=True)  # Field name made lowercase.

    class Meta:
         
        db_table = 'leave_requests'

    def __str__(self):
        return self.req_id