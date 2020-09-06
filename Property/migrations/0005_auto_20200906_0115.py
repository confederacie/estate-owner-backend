# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-06 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0004_auto_20200819_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='name',
            new_name='address2',
        ),
        migrations.RemoveField(
            model_name='property',
            name='neighbourhood',
        ),
        migrations.AddField(
            model_name='property',
            name='address1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='zipcode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='propertytype',
            field=models.CharField(choices=[('townhouse', 'Townhouse'), ('condo', 'Condo'), ('apartment', 'Apartment'), ('commercial', 'Commercial')], default='townhouse', max_length=2),
        ),
    ]