# Generated by Django 2.0.13 on 2019-04-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0010_auto_20190410_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformrun',
            name='status',
            field=models.CharField(choices=[(0, 'Started'), (1, 'Finished'), (2, 'Errored')], max_length=100),
        ),
    ]
