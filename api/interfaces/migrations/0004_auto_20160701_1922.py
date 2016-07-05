# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0003_auto_20160701_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='app_icon',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_long_description',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Long Description'),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_short_description',
            field=models.CharField(blank=True, max_length=128, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_url',
            field=models.URLField(blank=True, verbose_name='URL'),
        ),
    ]