# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20170407_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpicture',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
