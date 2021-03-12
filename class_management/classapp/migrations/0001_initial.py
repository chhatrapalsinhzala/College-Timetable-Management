# Generated by Django 3.0.1 on 2021-03-12 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('short_name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('class_date', models.DateTimeField(blank=True, null=True, verbose_name='Class date')),
                ('weekday', models.CharField(max_length=20, null=True, verbose_name='Weekday')),
                ('duration', models.CharField(max_length=255, verbose_name='Class Duration')),
                ('class_status', models.CharField(choices=[('scheduled', 'Scheduled'), ('cancelled', 'Cancelled')], default='scheduled', max_length=200, verbose_name='Class status')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_definition_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_definition_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
