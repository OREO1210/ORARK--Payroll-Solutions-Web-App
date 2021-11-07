# Generated by Django 2.2 on 2021-11-07 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_hod', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_receptionist', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Non-Binary')], default=2)),
                ('images', models.ImageField(blank=True, db_column='Images', default='/pics/orark-small.jpg', upload_to='pics')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('desg_id', models.BigAutoField(db_column='Desg_id', primary_key=True, serialize=False)),
                ('desgname', models.CharField(db_column='DesgName', max_length=100)),
                ('amount', models.FloatField(db_column='Amount')),
            ],
            options={
                'db_table': 'designation',
            },
        ),
        migrations.CreateModel(
            name='SlabTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llim', models.FloatField(db_column='Lower_Limit')),
                ('ulim', models.FloatField(db_column='Upper_Limit')),
                ('itax', models.FloatField(db_column='Income_Tax')),
                ('ptax', models.FloatField(db_column='Professional_Tax')),
                ('esic', models.FloatField(db_column='ESIC')),
            ],
            options={
                'db_table': 'slab_table',
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dep_id', models.BigIntegerField(db_column='Dep_id')),
                ('deptname', models.CharField(db_column='DeptName', max_length=100)),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('emp_id', models.BigIntegerField(db_column='Emp_id')),
                ('dob', models.DateField(db_column='DOB')),
                ('contact', models.CharField(db_column='Contact', max_length=18)),
                ('addresses', models.CharField(db_column='Addresses', max_length=700)),
                ('hire_date', models.DateField(db_column='Hire_date')),
                ('no_of_children', models.IntegerField(db_column='No_of_Children')),
                ('pannum', models.CharField(db_column='PAN', max_length=10)),
                ('pfnum', models.CharField(db_column='PF_Account_Num', max_length=22)),
                ('bank', models.CharField(choices=[('Union Bank of India', 'Union Bank of India'), ('Indian Bank', 'Indian Bank'), ('AU Small Finance Bank', 'AU Small Finance Bank'), ('Axis Bank', 'Axis Bank'), ('Bank of Baroda', 'Bank of Baroda'), ('Bank of India', 'Bank of India'), ('Bank of Maharashtra', 'Bank of Maharashtra'), ('Central Bank of India', 'Central Bank of India'), ('Canara Bank', 'Canara Bank'), ('Catholic Syrian Bank', 'Catholic Syrian Bank'), ('Citi Bank', 'Citi Bank'), ('DCB Bank', 'DCB Bank'), ('Dena Bank', 'Dena Bank'), ('Dhanalakshmi Bank', 'Dhanalakshmi Bank'), ('Equitas Small Finance Bank', 'Equitas Small Finance Bank'), ('Federal Bank', 'Federal Bank'), ('HDFC Bank', 'HDFC Bank'), ('HSBC Bank', 'HSBC Bank'), ('ICICI Bank', 'ICICI Bank'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('IndusInd Bank', 'IndusInd Bank'), ('IDBI Bank', 'IDBI Bank'), ('IDFC Bank', 'IDFC Bank'), ('Jammu and Kashmir Bank', 'Jammu and Kashmir Bank'), ('Karnataka Bank', 'Karnataka Bank'), ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'), ('Punjab National Bank', 'Punjab National Bank'), ('Punjab and Sind Bank', 'Punjab and Sind Bank'), ('RBL Bank', 'RBL Bank'), ('Standard Chartered Bank', 'Standard Chartered Bank'), ('State Bank Of India', 'State Bank Of India'), ('South Indian Bank', 'South Indian Bank'), ('UCO Bank', 'UCO Bank'), ('UYI Bank', 'UYI Bank'), ('Yes Bank', 'Yes Bank')], db_column='Bank_Name', max_length=100)),
                ('bankaccnum', models.CharField(db_column='Bank_Account_Num', max_length=18)),
                ('dep', models.ForeignKey(db_column='Dep_id', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Dept')),
                ('desg', models.ForeignKey(db_column='Desg_id', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Designation')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='MonthlySalary',
            fields=[
                ('slip_id', models.AutoField(db_column='Slip_id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
                ('month', models.IntegerField(blank=True, db_column='Month', null=True)),
                ('workingdays', models.IntegerField(blank=True, db_column='Working_Days', null=True)),
                ('absentdays', models.IntegerField(blank=True, db_column='Absent_Days', null=True)),
                ('paydays', models.IntegerField(blank=True, db_column='Pay_Days', null=True)),
                ('basic', models.FloatField(db_column='BASIC')),
                ('othr', models.IntegerField(db_column='OT_HR')),
                ('otpay', models.FloatField(db_column='OTPAY')),
                ('da', models.FloatField(db_column='DA')),
                ('pf', models.FloatField(db_column='PF')),
                ('esic', models.FloatField(db_column='ESIC')),
                ('itax', models.FloatField(db_column='ITAX')),
                ('ptax', models.FloatField(db_column='PTAX')),
                ('bonus', models.FloatField(blank=True, db_column='BONUS', null=True)),
                ('ma', models.FloatField(blank=True, db_column='MA', null=True)),
                ('ta', models.FloatField(blank=True, db_column='TA', null=True)),
                ('hra', models.FloatField(blank=True, db_column='HRA', null=True)),
                ('cea', models.FloatField(blank=True, db_column='CEA', null=True)),
                ('total', models.FloatField(blank=True, db_column='Total', null=True)),
                ('emp', models.ForeignKey(db_column='Emp_id', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Employees')),
            ],
            options={
                'db_table': 'monthly_salary',
            },
        ),
        migrations.AddField(
            model_name='designation',
            name='dep',
            field=models.ForeignKey(db_column='Dep_id', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Dept'),
        ),
    ]
