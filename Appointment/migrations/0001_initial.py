# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-14 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('response', models.CharField(choices=[('accept', 'Accept'), ('reschedule', 'Reschedule'), ('reject', 'Reject')], default=None, max_length=2, null=True)),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
