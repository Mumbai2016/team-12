# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_ngo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority_Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NGO_name', models.TextField()),
                ('priority_area', models.CharField(choices=[('PR', 'Program'), ('IM', 'Impact'), ('EX', 'External recognition'), ('FU', 'Funding'), ('TA', 'Talent')], max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='ngo',
            old_name='description',
            new_name='sdescription',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='priority_area',
        ),
        migrations.AddField(
            model_name='project',
            name='NGO_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategy',
            name='NGO_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategy',
            name='priority_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategy',
            name='strategy_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]