# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-26 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_auto_20170126_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prd_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]
