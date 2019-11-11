# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-03 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleDashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('titulo', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]