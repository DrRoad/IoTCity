# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0027_auto_20170420_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmactuator',
            old_name='subscription',
            new_name='subscriptions',
        ),
    ]