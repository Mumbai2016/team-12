# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_project_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='status',
            field=models.CharField(choices=[('NS', 'Not started'), ('ON', 'Ongoing'), ('PO', 'Postponed'), ('AB', 'Aborted'), ('CO', 'Completed')], max_length=20),
        ),
    ]
