# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='handle_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]