# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]