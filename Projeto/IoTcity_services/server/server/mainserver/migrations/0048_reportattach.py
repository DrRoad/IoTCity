# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0047_userreport_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportAttach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
