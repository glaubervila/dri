# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-02 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userquery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]