# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-03 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20170503_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
