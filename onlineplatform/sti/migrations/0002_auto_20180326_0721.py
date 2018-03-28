# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sti', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['language'], name='sti_store_languag_446771_idx'),
        ),
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['partner'], name='sti_store_partner_bbcb2c_idx'),
        ),
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['store_type'], name='sti_store_store_t_e315ee_idx'),
        ),
    ]
