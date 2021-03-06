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
BANK_CHOICES = [('Union Bank of India','Union Bank of India'),
                ('Indian Bank','Indian Bank'),
                ('AU Small Finance Bank','AU Small Finance Bank'),
                ('Axis Bank','Axis Bank'),
                ('Bank of Baroda','Bank of Baroda'),
                ('Bank of India','Bank of India'),
                ('Bank of Maharashtra','Bank of Maharashtra'),
                ('Central Bank of India','Central Bank of India'),
                ('Canara Bank','Canara Bank'),
                ('Catholic Syrian Bank','Catholic Syrian Bank'),
                ('Citi Bank','Citi Bank'),
                ('DCB Bank','DCB Bank'),
                ('Dena Bank','Dena Bank'),
                ('Dhanalakshmi Bank','Dhanalakshmi Bank'),
                ('Equitas Small Finance Bank','Equitas Small Finance Bank'),
                ('Federal Bank','Federal Bank'),
                ('HDFC Bank','HDFC Bank'),
                ('HSBC Bank','HSBC Bank'),
                ('ICICI Bank','ICICI Bank'),
                ('Indian Overseas Bank','Indian Overseas Bank'),
                ('IndusInd Bank','IndusInd Bank'),
                ('IDBI Bank','IDBI Bank'),
                ('IDFC Bank','IDFC Bank'),
                ('Jammu and Kashmir Bank','Jammu and Kashmir Bank'),
                ('Karnataka Bank','Karnataka Bank'),
                ('Kotak Mahindra Bank','Kotak Mahindra Bank'),
                ('Punjab National Bank','Punjab National Bank'),
                ('Punjab and Sind Bank','Punjab and Sind Bank'),
                ('RBL Bank','RBL Bank'),
                ('Standard Chartered Bank','Standard Chartered Bank'),
                ('State Bank Of India','State Bank Of India'),
                ('South Indian Bank','South Indian Bank'),
                ('UCO Bank','UCO Bank'),
                ('UYI Bank','UYI Bank'),
                ('Yes Bank','Yes Bank')]



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
    is_receptionist=models.BooleanField(default=False)
    username = None
    email = models.EmailField(('email address'), unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=2)
    images = models.ImageField(db_column='Images', upload_to='pics',default='/pics/orark-small.png', blank=True)   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email  


class MonthlySalary(models.Model):
    slip_id = models.AutoField(db_column='Slip_id', primary_key=True)   
    emp = models.ForeignKey('Employees', models.DO_NOTHING, db_column='Emp_id')   
    year = models.IntegerField(db_column='Year', blank=True, null=True)  
    month = models.IntegerField(db_column='Month', blank=True, null=True)  
    workingdays = models.IntegerField(db_column='Working_Days', blank=True, null=True)  
    absentdays = models.IntegerField(db_column='Absent_Days', blank=True, null=True)  
    paydays = models.IntegerField(db_column='Pay_Days', blank=True, null=True)  
    basic = models.FloatField(db_column='BASIC')   
    othr = models.IntegerField(db_column='OT_HR')   
    otpay = models.FloatField(db_column='OTPAY')   
    da = models.FloatField(db_column='DA')   
    pf = models.FloatField(db_column='PF')   
    esic = models.FloatField(db_column='ESIC')   
    itax = models.FloatField(db_column='ITAX')   
    ptax = models.FloatField(db_column='PTAX')   
    bonus = models.FloatField(db_column='BONUS', blank=True, null=True)   
    ma = models.FloatField(db_column='MA', blank=True, null=True)   
    ta = models.FloatField(db_column='TA', blank=True, null=True)   
    hra = models.FloatField(db_column='HRA', blank=True, null=True)   
    cea = models.FloatField(db_column='CEA', blank=True, null=True)   
    gded = models.FloatField(db_column='gded', blank=True, null=True)   
    gearn = models.FloatField(db_column='gearn', blank=True, null=True)   
    total = models.FloatField(db_column='Total', blank=True, null=True)   

    class Meta:
        db_table = 'monthly_salary'
    
    def __str__(self):
        return self.year.__str__()+' | '+self.month.__str__()+' | '+self.emp.emp_id.__str__()
    
    


class SlabTable(models.Model):
    llim = models.FloatField(db_column='Lower_Limit')   
    ulim = models.FloatField(db_column='Upper_Limit')   
    itax = models.FloatField(db_column='Income_Tax')   
    ptax = models.FloatField(db_column='Professional_Tax')   
    esic = models.FloatField(db_column='ESIC')   
    
    class Meta:
        db_table = 'slab_table'
    
    def __str__(self):
        return self.llim.__str__() + ' - ' + self.ulim.__str__()

    


class Dept(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    dep_id = models.BigIntegerField(db_column='Dep_id', null=False)   
    deptname = models.CharField(db_column='DeptName', max_length=100)   
   
    class Meta:
         
        db_table = 'dept'
    
    def __str__(self):
        return self.deptname
    


class Designation(models.Model):
    desg_id = models.BigAutoField(db_column='Desg_id', primary_key=True)   
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')   
    desgname = models.CharField(db_column='DesgName', max_length=100)   
    amount = models.FloatField(db_column='Amount')   

    class Meta:
        db_table = 'designation'
    
    def __str__(self):
        return self.dep.deptname+' | ' + self.desgname
    


class Employees(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    emp_id = models.BigIntegerField(db_column='Emp_id', null=False)   
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')   
    desg = models.ForeignKey(Designation, models.DO_NOTHING, db_column='Desg_id')   
    dob = models.DateField(db_column='DOB')   
    contact = models.CharField(max_length=18,db_column='Contact')   
    addresses = models.CharField(db_column='Addresses', max_length=700)   
    hire_date = models.DateField(db_column='Hire_date')   
    no_of_children = models.IntegerField(db_column='No_of_Children')   
    pannum = models.CharField(max_length=10,db_column='PAN')   
    pfnum = models.CharField(max_length=22,db_column='PF_Account_Num')   
    bank = models.CharField(choices=BANK_CHOICES,max_length=100,db_column='Bank_Name')   
    bankaccnum = models.CharField(max_length=18,db_column='Bank_Account_Num')   
    

    class Meta:
         
        db_table = 'employees'
    
    def __str__(self):
        return self.user.email
    
