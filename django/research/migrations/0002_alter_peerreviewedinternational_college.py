# Generated by Django 3.2.3 on 2021-06-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerreviewedinternational',
            name='college',
            field=models.CharField(choices=[('CBE', 'COLLEGE OF BUSINESS AND ECONOMY'), ('CST', 'COLLEGE OF SCIENCE AND TECHNOLOGY')], max_length=100),
        ),
    ]
