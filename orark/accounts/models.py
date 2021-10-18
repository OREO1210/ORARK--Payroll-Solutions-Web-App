from django.db import models

# Create your models here.

class BaseSalary(models.Model):
    salary_id = models.BigIntegerField(db_column='Salary_id', primary_key=True)  # Field name made lowercase.
    dep = models.ForeignKey('Dept', models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desg = models.ForeignKey('Designation', models.DO_NOTHING, db_column='Desg_id')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    da = models.FloatField(db_column='DA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'base_salary'


class ComplementarySalary(models.Model):
    comp_id = models.BigIntegerField(db_column='Comp_id', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('Employees', models.DO_NOTHING, db_column='Emp_id')  # Field name made lowercase.
    bonus = models.FloatField(db_column='BONUS', blank=True, null=True)  # Field name made lowercase.
    ma = models.FloatField(db_column='MA', blank=True, null=True)  # Field name made lowercase.
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    per_inc = models.IntegerField(db_column='per_INC', blank=True, null=True)  # Field name made lowercase.
    cea = models.FloatField(db_column='CEA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'complementary_salary'


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


class Dept(models.Model):
    dep_id = models.BigIntegerField(db_column='Dep_id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=100)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.

    class Meta:
         
        db_table = 'dept'


class Designation(models.Model):
    desg_id = models.BigIntegerField(db_column='Desg_id', primary_key=True)  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desgname = models.CharField(db_column='DesgName', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'designation'


class Employees(models.Model):
    emp_id = models.BigIntegerField(db_column='Emp_id', primary_key=True)  # Field name made lowercase.
    dep = models.ForeignKey(Dept, models.DO_NOTHING, db_column='Dep_id')  # Field name made lowercase.
    desg = models.ForeignKey(Designation, models.DO_NOTHING, db_column='Desg_id')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    passwords = models.CharField(db_column='Passwords', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact')  # Field name made lowercase.
    addresses = models.CharField(db_column='Addresses', max_length=700)  # Field name made lowercase.
    images = models.CharField(db_column='Images', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hire_date = models.DateField(db_column='Hire_date')  # Field name made lowercase.
    metrocity = models.IntegerField(db_column='Metrocity')  # Field name made lowercase.
    no_of_children = models.IntegerField(db_column='No_of_Children')  # Field name made lowercase.

    class Meta:
         
        db_table = 'employees'


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