# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0013_publication_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='press',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='publication',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='work',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
    ]
