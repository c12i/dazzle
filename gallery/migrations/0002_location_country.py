# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-09 13:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 13, 42, 17, 114872, tzinfo=utc), max_length=244),
            preserve_default=False,
        ),
    ]
