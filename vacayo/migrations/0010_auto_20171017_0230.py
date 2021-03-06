# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 02:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacayo', '0009_auto_20171009_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='first_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='last_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
