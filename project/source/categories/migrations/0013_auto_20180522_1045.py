# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-22 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0012_category_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='picture',
            new_name='image',
        ),
    ]
