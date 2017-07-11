# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0011_remove_experiment_success_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='dashboard_image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('Started', 'Started'), ('Complete', 'Complete'), ('Rejected', 'Rejected'), ('Invalid', 'Invalid')], default='Not Started', max_length=255),
        ),
    ]