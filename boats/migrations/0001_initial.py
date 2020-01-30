# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-30 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='', max_length=254)),
                ('boatType', models.CharField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('maxPassangers', models.DecimalField(decimal_places=0, max_digits=2)),
                ('cabins', models.DecimalField(decimal_places=0, max_digits=2)),
                ('lenght', models.DecimalField(decimal_places=2, max_digits=6)),
                ('builtDate', models.DateField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
