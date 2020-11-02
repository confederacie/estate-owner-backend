# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-14 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Appointment', '0001_initial'),
        ('User', '0001_initial'),
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_id', to='User.Buyer'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_id', to='Property.Property'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='User.Seller'),
        ),
    ]