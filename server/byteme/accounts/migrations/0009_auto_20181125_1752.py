# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-25 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20181125_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='speakerEmail',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]