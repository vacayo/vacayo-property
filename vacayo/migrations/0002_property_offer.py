# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacayo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='offer',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
