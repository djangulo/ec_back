# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 17:12
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=accounts.models.user_directory_path)),
                ('bio', models.TextField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('staff_or_intern', models.IntegerField(choices=[(0, 'Neither'), (1, 'Estudio Caribe Staff'), (2, 'Estudio Caribe Intern')], default=0, verbose_name='Is staff or intern?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
