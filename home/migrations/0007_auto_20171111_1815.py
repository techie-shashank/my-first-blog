# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171111_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(default='MEDIA_ROOT/images/back.jpg', upload_to=''),
        ),
    ]
