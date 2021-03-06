# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacayo', '0017_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[(b'Ready', b'Ready'), (b'Pending Lease Signing', b'Pending Lease Signing'), (b'Pending Superhost Assignment', b'Pending Superhost Assignment'), (b'Pending Site Visit', b'Pending Site Visit'), (b'New', b'New'), (b'Pending Review', b'Pending Review')], default=b'New', max_length=256),
        ),
    ]
