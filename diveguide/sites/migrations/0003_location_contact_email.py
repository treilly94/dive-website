# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='contact_email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
