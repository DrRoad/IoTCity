# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0035_auto_20170425_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorsubtype',
            name='subtype',
        ),
    ]