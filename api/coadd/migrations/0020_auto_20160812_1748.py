# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-12 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0019_survey_srv_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='image_src_ptif',
            field=models.URLField(blank=True, default=None, help_text='url complete for visiomatic ptif image, including the host and directory.use the release name and tilename to create the path. example: http://{host}/data/releases/{release_name}/images/visiomatic/{tilename}.ptif', null=True, verbose_name='Visiomatic PTIF'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='image_src_thumbnails',
            field=models.URLField(blank=True, default=None, help_text='Full url to image including the host and directory. example: http://{host}/data/releases/{release_name}/images/thumb', null=True, verbose_name='Thumbnails PNG'),
        ),
    ]
