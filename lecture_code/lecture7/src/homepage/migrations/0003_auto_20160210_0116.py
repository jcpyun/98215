# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_blog_checklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='checklist',
            field=models.NullBooleanField(default='false'),
        ),
    ]
