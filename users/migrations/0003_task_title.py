# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170226_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
