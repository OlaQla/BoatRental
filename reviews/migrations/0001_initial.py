# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 19:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('reviewText',
                 models.CharField(
                     default='',
                     max_length=254)),
                ('starRating',
                 models.IntegerField(
                     default=5,
                     validators=[
                         django.core.validators.MaxValueValidator(5),
                         django.core.validators.MinValueValidator(1)])),
                ('image',
                 models.ImageField(
                     upload_to='images')),
            ],
        ),
    ]
