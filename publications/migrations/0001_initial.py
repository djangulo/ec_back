# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import publications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='press_releases', to='publications.Category')),
            ],
            options={
                'verbose_name': 'press release',
                'verbose_name_plural': 'press releases',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('medium', models.IntegerField(choices=[(0, 'Article'), (1, 'Review'), (2, 'Book'), (3, 'Blogpost')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to=publications.models.publication_directory_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publications.Category')),
            ],
            options={
                'verbose_name': 'publication',
                'verbose_name_plural': 'publications',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('program', models.CharField(max_length=75)),
                ('status', models.IntegerField(choices=[(0, 'Planned'), (1, 'Under Construction'), (2, 'Completed')])),
                ('team', models.TextField(default='')),
                ('date_released', models.DateField()),
                ('document', models.FileField(blank=True, null=True, upload_to=publications.models.work_directory_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='publications.Category')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
            },
        ),
        migrations.CreateModel(
            name='WorkPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=publications.models.work_directory_path)),
                ('caption', models.TextField()),
                ('is_cover', models.BooleanField(default=False, help_text="If yes, this image will be the cover of the 'Work' entry it belongs to.")),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='publications.Work')),
            ],
        ),
    ]