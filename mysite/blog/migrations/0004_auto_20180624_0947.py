# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180624_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 1, 47, 57, 421608, tzinfo=utc)),
        ),
    ]
