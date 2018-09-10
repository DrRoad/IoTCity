# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0006_subscription_subtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensorsubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtype', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainserver.Sensorsubtype'),
        ),
    ]