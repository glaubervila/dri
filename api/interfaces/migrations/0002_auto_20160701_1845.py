# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='app_url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]