# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.DecimalField(decimal_places=1, max_digits=3)),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('name', models.CharField(max_length=200)),
                ('director', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Director')),
                ('genere', models.ManyToManyField(to='movieapp.Genere')),
            ],
        ),
    ]
