# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0016_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(blank=True, max_length=30, null=True, verbose_name='Run')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag_tile',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag_tile',
            name='tile',
        ),
        migrations.AlterField(
            model_name='tag',
            name='tiles',
            field=models.ManyToManyField(through='coadd.Dataset', to='coadd.Tile'),
        ),
        migrations.DeleteModel(
            name='Tag_Tile',
        ),
        migrations.AddField(
            model_name='dataset',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coadd.Tag'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coadd.Tile'),
        ),
    ]
