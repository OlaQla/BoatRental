# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-16 19:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_auto_20200210_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
