# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_auto_20170422_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcover',
            name='work',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='publications.Work'),
        ),
        migrations.AlterField(
            model_name='workpicture',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='publications.Work'),
        ),
    ]
