# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_auto_20180424_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f', max_length=4096, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
    ]