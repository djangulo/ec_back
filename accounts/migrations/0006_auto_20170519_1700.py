# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170509_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='linked_in',
            field=models.URLField(blank=True, default=''),
        ),
    ]
