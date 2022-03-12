# Generated by Django 3.2.9 on 2022-03-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0011_alter_notifications_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('profile', models.ImageField(upload_to='images/')),
                ('contact', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
