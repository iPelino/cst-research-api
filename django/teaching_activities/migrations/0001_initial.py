# Generated by Django 3.2.3 on 2021-06-07 14:21

from django.db import migrations, models
import teaching_activities.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teaching_portofolio',
            fields=[
                ('certificate_id', models.CharField(default=teaching_activities.models.Teaching_portofolio.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('TP_name', models.CharField(max_length=100)),
                ('TP_Developed', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='THLIC_Certificate',
            fields=[
                ('certificate_id', models.CharField(default=teaching_activities.models.THLIC_Certificate.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('certificate_name', models.CharField(max_length=100)),
                ('certificate_obtained_Yes_Or_No', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
    ]
