# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-27 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='country',
            field=models.CharField(choices=[('u', 'usa'), ('e', 'england')], max_length=255),
        ),
        migrations.AlterField(
            model_name='header',
            name='currency',
            field=models.CharField(choices=[('d', 'dollar'), ('p', 'pound')], max_length=255),
        ),
    ]