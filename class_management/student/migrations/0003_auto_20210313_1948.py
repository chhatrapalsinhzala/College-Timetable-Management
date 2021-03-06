# Generated by Django 3.1.7 on 2021-03-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='student',
            name='state',
        ),
        migrations.RemoveField(
            model_name='student',
            name='street',
        ),
        migrations.RemoveField(
            model_name='student',
            name='street_2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='zip',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
    ]
