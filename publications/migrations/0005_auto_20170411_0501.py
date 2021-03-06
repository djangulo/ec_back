# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressrelease',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='publication',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='work',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workpicture',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
