# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20180129_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='99popularity',
            new_name='popularity',
        ),
    ]