# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-31 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
