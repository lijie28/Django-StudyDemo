# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20170809_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category_id',
            new_name='category',
        ),
    ]
