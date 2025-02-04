# Generated by Django 2.2.10 on 2020-06-24 21:02

from django.db import migrations

from fetcher.helpers import identifier_from_uri


class Migration(migrations.Migration):

    def generate_identifiers(apps, schema_editor):
        DataObject = apps.get_model('transformer', 'DataObject')
        for obj in DataObject.objects.all():
            obj.es_id = identifier_from_uri(obj.uri)
            obj.save()

    def reverse_gen_identifiers(apps, schema_editor):
        pass

    dependencies = [
        ('transformer', '0003_auto_20200623_1344'),
    ]

    operations = [
        migrations.RunPython(generate_identifiers, reverse_gen_identifiers)
    ]
