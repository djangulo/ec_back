# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0011_auto_20170422_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField(blank=True, help_text='URL to external resource or additional info')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presses', to='publications.Category')),
            ],
            options={
                'verbose_name': 'press release',
                'verbose_name_plural': 'press releases',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='pressrelease',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='workcover',
            options={'verbose_name': 'cover', 'verbose_name_plural': 'cover'},
        ),
        migrations.DeleteModel(
            name='PressRelease',
        ),
    ]
