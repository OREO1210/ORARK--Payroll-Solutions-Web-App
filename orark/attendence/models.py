from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django import forms
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import *

class Attendence(models.Model):
    today_date = models.DateField(db_column='Date', default=datetime.datetime.now)  # Field name made lowercase.
    entry_time = models.TimeField(db_column='Entry Time')
    exit_time = models.TimeField(db_column='Exit Time')
    emp = models.ForeignKey(Employees, models.DO_NOTHING, db_column='Emp ID')  # Field name made lowercase.
    emaill=models.ForeignKey(User, models.DO_NOTHING, db_column='email id')
    working_hrs = models.CharField(max_length=100,db_column='Working hours', default='00:00') # Field name made lowercase Field name made lowercase.
    deptid = models.ForeignKey( Dept, models.DO_NOTHING, db_column='department ID')  # Field name made lowercase.
    att_id = models.AutoField(db_column='Attendence_id', primary_key=True) 
   
    class Meta:
         
        db_table = 'attendence'
    
    def __str__(self):
        return self.today_date + '|' + self.empid.user.email


