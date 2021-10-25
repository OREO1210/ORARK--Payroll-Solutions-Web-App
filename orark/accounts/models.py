from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django import forms
# Create your models here.

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NONBINARY=2
GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_NONBINARY, 'Non-Binary')]


yes=1
no=0
metrocity_choices=[(yes,'yes'),(no,'no')]

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    is_hod=models.BooleanField(default=False)
    is_employee=models.BooleanField(default=False)
    username = None
    email = models.EmailField(('email address'), unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=2)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
   
    
class BaseSalary(models.Model):
    salary_id = models.BigIntegerField(db_column='Salary_id', primary_key=True)  # Field name made lowercase.
    dep = models.ForeignKey('Dept', models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desg = models.ForeignKey('Designation', models.DO_NOTHING, db_column='Desg_id')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    da = models.FloatField(db_column='DA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'base_salary'

    def __str__(self):
        return self.dep.deptname
    


class ComplementarySalary(models.Model):
    comp_id = models.BigIntegerField(db_column='Comp_id', primary_key=True)  # Field name made lowercase.
    bonus = models.FloatField(db_column='BONUS', blank=True, null=True)  # Field name made lowercase.
    ma = models.FloatField(db_column='MA', blank=True, null=True)  # Field name made lowercase.
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    per_inc = models.IntegerField(db_column='per_INC', blank=True, null=True)  # Field name made lowercase.
    cea = models.FloatField(db_column='CEA', blank=True, null=True)  # Field name made lowercase.
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])

    class Meta:
        db_table = 'complementary_salary'
    
    def __str__(self):
        return self.year.__str__()
    

class Deductions(models.Model):
    ded_id = models.BigIntegerField(db_column='Ded_id', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('Employees', models.DO_NOTHING, db_column='Emp_id')  # Field name made lowercase.
    lop_days = models.IntegerField(db_column='LOP_days', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF')  # Field name made lowercase.
    esic = models.FloatField(db_column='ESIC')  # Field name made lowercase.
    tax = models.FloatField(db_column='TAX')  # Field name made lowercase.
    lwf = models.FloatField(db_column='LWF', blank=True, null=True)  # Field name made lowercase.
    nps = models.FloatField(db_column='NPS', blank=True, null=True)  # Field name made lowercase.
    lop = models.FloatField(db_column='LOP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'deductions'
    
    def __str__(self):
        return self.emp.user.first_name + ' ' + self.emp.user.last_name
    

class Dept(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    dep_id = models.BigIntegerField(db_column='Dep_id', null=False)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=100)  # Field name made lowercase.
   
    class Meta:
         
        db_table = 'dept'
    
    def __str__(self):
        return self.deptname
    


class Designation(models.Model):
    desg_id = models.BigIntegerField(db_column='Desg_id', primary_key=True)  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desgname = models.CharField(db_column='DesgName', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'designation'
    
    def __str__(self):
        return self.dep.deptname+' | ' + self.desgname
    


class Employees(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    emp_id = models.BigIntegerField(db_column='Emp_id', null=False)  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desg = models.ForeignKey(Designation, models.DO_NOTHING, db_column='Desg_id')  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    contact = models.CharField(max_length=18,db_column='Contact')  # Field name made lowercase.
    addresses = models.CharField(db_column='Addresses', max_length=700)  # Field name made lowercase.
    images = models.CharField(db_column='Images', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hire_date = models.DateField(db_column='Hire_date')  # Field name made lowercase.
    metrocity = models.IntegerField(choices=metrocity_choices,default=2)
    no_of_children = models.IntegerField(db_column='No_of_Children')  # Field name made lowercase.

    class Meta:
         
        db_table = 'employees'
    
    def __str__(self):
        return self.user.email
    

class LeaveRequests(models.Model):
    req_id = models.BigIntegerField(db_column='Req_id', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey(Employees, models.DO_NOTHING, db_column='Emp_id')  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    leave_date = models.DateField(db_column='Leave_Date')  # Field name made lowercase.
    leave_type = models.CharField(db_column='Leave_Type', max_length=700)  # Field name made lowercase.
    applications = models.CharField(db_column='Applications', max_length=700, blank=True, null=True)  # Field name made lowercase.
    statuses = models.IntegerField(db_column='Statuses')  # Field name made lowercase.
    lop = models.IntegerField(db_column='LOP')  # Field name made lowercase.
    date_of_application = models.DateField(db_column='Date_of_application', blank=True, null=True)  # Field name made lowercase.

    class Meta:
         
        db_table = 'leave_requests'

    def __str__(self):
        return self.req_id
    