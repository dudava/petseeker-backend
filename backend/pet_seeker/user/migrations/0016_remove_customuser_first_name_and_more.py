# Generated by Django 5.0.6 on 2024-07-24 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_customuser_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
