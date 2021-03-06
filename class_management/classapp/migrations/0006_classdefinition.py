# Generated by Django 3.1.7 on 2021-03-14 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0006_remove_staff_subjects'),
        ('classapp', '0005_delete_classdefinition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('class_date', models.DateField(verbose_name='Class date')),
                ('duration', models.CharField(max_length=255, verbose_name='Class Duration')),
                ('class_status', models.CharField(choices=[('scheduled', 'scheduled'), ('cancelled', 'cancelled')], default='scheduled', max_length=200, verbose_name='Class status')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_definition_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_definition_modifier', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='staff.staff', verbose_name='Teacher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='classapp.subject', verbose_name='subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
