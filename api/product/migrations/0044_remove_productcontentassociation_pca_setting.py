# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-17 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_remove_product_prd_flag_removed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcontentassociation',
            name='pca_setting',
        ),
    ]