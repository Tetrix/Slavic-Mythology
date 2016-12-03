# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_tales'),
        ('stories', '0004_auto_20161203_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legends_and_traditions',
            name='form',
        ),
        migrations.AddField(
            model_name='legends_and_traditions',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile'),
        ),
    ]
