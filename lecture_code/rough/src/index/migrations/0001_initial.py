# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('context', models.TextField()),
                ('after', models.DateTimeField()),
                ('initial', models.DateTimeField()),
            ],
        ),
    ]
