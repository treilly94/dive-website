# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
