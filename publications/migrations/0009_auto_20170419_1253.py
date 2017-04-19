# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0008_auto_20170419_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medium',
            options={'verbose_name': 'medium', 'verbose_name_plural': 'mediums'},
        ),
        migrations.AddField(
            model_name='medium',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medium',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='url',
            field=models.URLField(blank=True, help_text='URL to external resource or additional info'),
        ),
        migrations.AlterField(
            model_name='program',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='publications.Category'),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
