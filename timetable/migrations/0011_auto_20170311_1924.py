# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-12 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_add_rows_to_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='semester',
            new_name='_semester',
        ),
    ]