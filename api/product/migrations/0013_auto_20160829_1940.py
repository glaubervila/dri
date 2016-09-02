# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-29 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0023_auto_20160826_1512'),
        ('product', '0012_auto_20160810_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='mpa_release',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='coadd.Release', verbose_name='Release'),
        ),
        migrations.AddField(
            model_name='map',
            name='mpa_tag',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='coadd.Tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='map',
            name='mpa_filter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Filter', verbose_name='Filter'),
        ),
    ]
