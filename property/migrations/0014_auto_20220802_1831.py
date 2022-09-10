# Generated by Django 2.2.24 on 2022-08-02 15:24

from django.db import migrations


def add_flats_to_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    owners = Owner.objects.all()
    for owner in owners:
        flats = Flat.objects.filter(owner=owner.owner,
                                    owner_pure_phone=owner.owner_pure_phone)
        if flats:
            owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220802_1831'),
    ]

    operations = [migrations.RunPython(add_flats_to_owners),
    ]