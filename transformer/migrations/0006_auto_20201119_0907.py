# Generated by Django 2.2.13 on 2020-11-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0005_remove_dataobject_uri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataobject',
            name='id',
        ),
        migrations.AlterField(
            model_name='dataobject',
            name='es_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
