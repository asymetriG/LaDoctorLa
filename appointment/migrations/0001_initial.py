# Generated by Django 5.0.4 on 2024-05-01 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentID', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('appointment_details', models.TextField()),
                ('granted', models.BooleanField(default=False)),
                ('is_taken', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.doctor')),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
            ],
        ),
    ]
