# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170419_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('display_order', 'last_name', 'first_name')},
        ),
        migrations.AddField(
            model_name='user',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
    ]