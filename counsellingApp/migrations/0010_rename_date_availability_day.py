# Generated by Django 3.2.9 on 2022-02-28 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0009_availability_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='date',
            new_name='day',
        ),
    ]
