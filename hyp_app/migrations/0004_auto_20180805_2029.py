# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-05 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hyp_app', '0003_mqttlog_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mqttlog',
            old_name='date',
            new_name='dateTime',
        ),
        migrations.RenameField(
            model_name='mqttlog',
            old_name='time',
            new_name='hourTime',
        ),
    ]
