# Generated by Django 5.0.6 on 2024-07-22 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0009_remove_privateannouncement_location_and_more'),
        ('user', '0013_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateannouncement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='user.customuser'),
        ),
    ]
