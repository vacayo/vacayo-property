# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacayo', '0014_auto_20171027_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='property',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='property',
            name='city',
        ),
        migrations.RemoveField(
            model_name='property',
            name='state',
        ),
        migrations.RemoveField(
            model_name='property',
            name='zip_code',
        ),
    ]
