# Generated by Django 4.0.2 on 2022-02-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_sportowiec_opis_sportowiec_zdjęcie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportowiec',
            old_name='rok',
            new_name='rok_urodzenia',
        ),
    ]
