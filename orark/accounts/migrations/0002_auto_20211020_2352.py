# Generated by Django 3.2.7 on 2021-10-20 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='eemail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pwd',
        ),
    ]
