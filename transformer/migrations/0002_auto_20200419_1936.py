# Generated by Django 2.2.10 on 2020-04-19 23:36

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='dataobject',
            index=django.contrib.postgres.indexes.GinIndex(fields=['data'], name='data_gin'),
        ),
    ]