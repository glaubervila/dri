# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=128, verbose_name='Internal Name')),
                ('app_url', models.CharField(max_length=128, verbose_name='URL')),
                ('app_short_description', models.CharField(max_length=128, verbose_name='Short Description')),
                ('app_long_description', models.CharField(max_length=1024, verbose_name='Long Description')),
                ('app_icon', models.ImageField(upload_to='')),
                ('app_thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]