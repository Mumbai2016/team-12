# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160724_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
