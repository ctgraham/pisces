# Generated by Django 2.0.13 on 2019-04-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0008_auto_20190410_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='title',
            field=models.CharField(blank=True, max_length=16384, null=True),
        ),
    ]