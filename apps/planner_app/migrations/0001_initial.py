# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20180219_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('playlist', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('preperation', models.CharField(max_length=255)),
                ('materials', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='login_app.User')),
            ],
        ),
    ]