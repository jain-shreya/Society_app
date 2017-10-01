# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile_home',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('en_no', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ph_no', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('profile_pic', models.CharField(max_length=250)),
            ],
        ),
    ]
