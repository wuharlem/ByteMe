# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20181124_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
