# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180624_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Four',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocabularys', models.CharField(max_length=100)),
                ('paraphrases', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Six',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocabularys', models.CharField(max_length=100)),
                ('paraphrases', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Toefl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocabularys', models.CharField(max_length=100)),
                ('paraphrases', models.CharField(max_length=300)),
            ],
        ),
    ]
