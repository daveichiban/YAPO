# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0029_auto_20160716_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='scene_tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='websites', to='videos.SceneTag'),
        ),
    ]
