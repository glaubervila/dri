# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_classifier', '0003_productgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='pcl_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_classifier.ProductGroup'),
            preserve_default=False,
        ),
    ]
