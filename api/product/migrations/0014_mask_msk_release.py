# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-01 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0023_auto_20160826_1512'),
        ('product', '0013_auto_20160829_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='mask',
            name='msk_release',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='coadd.Release', verbose_name='Release'),
        ),
    ]
