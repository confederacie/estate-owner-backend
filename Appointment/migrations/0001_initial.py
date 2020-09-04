# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-04 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_auto_20200831_2249'),
        ('Property', '0004_auto_20200819_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('response', models.CharField(choices=[('accept', 'Accept'), ('reschedule', 'Reschedule'), ('reject', 'Reject')], default=None, max_length=2)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_id', to='User.Buyer')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_id', to='Property.Property')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='User.Seller')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
