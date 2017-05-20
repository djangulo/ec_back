# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0012_auto_20170422_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='url',
            field=models.URLField(blank=True, help_text='URL to external resource or additional info'),
        ),
    ]
