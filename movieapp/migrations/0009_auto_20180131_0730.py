# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0008_auto_20180130_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Director'),
        ),
    ]
