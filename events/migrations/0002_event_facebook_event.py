# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='facebook_event',
            field=models.URLField(blank=True),
        ),
    ]
