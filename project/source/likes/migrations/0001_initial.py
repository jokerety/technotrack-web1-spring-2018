# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-24 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0005_task_usertask'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u041b\u0430\u0439\u043a \u043d\u0430\u0436\u0430\u0442')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='task.Task', verbose_name='\u0417\u0430\u0434\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': ' \u041b\u0430\u0439\u043a',
                'verbose_name_plural': '\u041b\u0430\u0439\u043a\u0438',
            },
        ),
    ]
