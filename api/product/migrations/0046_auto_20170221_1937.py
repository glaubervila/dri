# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-21 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_auto_20170216_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutout',
            name='ctt_file_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Filename '),
        ),
        migrations.AlterField(
            model_name='cutout',
            name='ctt_file_path',
            field=models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='File Path'),
        ),
        migrations.AlterField(
            model_name='cutout',
            name='ctt_file_type',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, verbose_name='File Extension'),
        ),
    ]
