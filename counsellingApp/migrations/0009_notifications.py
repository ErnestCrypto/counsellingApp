# Generated by Django 3.2.9 on 2022-03-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0008_auto_20220311_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsellor_id', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
