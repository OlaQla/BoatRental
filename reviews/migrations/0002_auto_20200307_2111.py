# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name_plural': 'Reviews'},
        ),
    ]