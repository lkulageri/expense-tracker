# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-30 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_auto_20190129_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_k',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
