# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 02:28
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import modules.landing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('imagen', models.ImageField(upload_to=modules.landing.models.user_directory_path)),
            ],
        ),
    ]
