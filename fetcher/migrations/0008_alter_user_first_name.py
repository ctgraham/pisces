# Generated by Django 3.2.5 on 2021-07-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetcher', '0007_auto_20200313_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
