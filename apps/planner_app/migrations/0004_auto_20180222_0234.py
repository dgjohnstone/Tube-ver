# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-22 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0003_auto_20180220_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='edited',
        ),
        migrations.RemoveField(
            model_name='video',
            name='posted',
        ),
        migrations.RemoveField(
            model_name='video',
            name='scripted',
        ),
        migrations.RemoveField(
            model_name='video',
            name='shot',
        ),
    ]
