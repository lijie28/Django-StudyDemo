# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170809_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]
