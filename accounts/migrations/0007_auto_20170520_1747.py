# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170519_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='linked_in',
            new_name='linkedin',
        ),
    ]
