# Generated by Django 3.1.7 on 2021-03-13 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20210313_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='subjects',
        ),
    ]
