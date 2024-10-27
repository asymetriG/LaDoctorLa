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
            name='MedicalReport',
            fields=[
                ('reportID', models.AutoField(primary_key=True, serialize=False)),
                ('report_date', models.DateField()),
                ('report_time', models.TimeField()),
                ('report_content', models.TextField()),
                ('URL', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
            ],
        ),
    ]
