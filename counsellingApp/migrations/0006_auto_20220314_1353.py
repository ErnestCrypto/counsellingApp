# Generated by Django 3.2.9 on 2022-03-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0005_notifications_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='subject',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
