# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('coadd', '0009_auto_20160420_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='filter',
            field=models.CharField(max_length=3, verbose_name='Filter'),
        ),
    ]
