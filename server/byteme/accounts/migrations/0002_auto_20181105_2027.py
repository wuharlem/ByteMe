# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181102_1725'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]
