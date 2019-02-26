# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-02-24 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='actuador_record_state',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='cycle',
            name='days',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='cycle',
            name='end_cycle',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cycle',
            name='start_cycle',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cycle',
            name='title',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='cycle',
            name='total_cycle',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peripheral',
            name='data_metric',
            field=models.CharField(default='', max_length=10),
        ),
    ]