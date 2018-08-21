# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20180320_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_archieve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='categories.Category'),
        ),
    ]