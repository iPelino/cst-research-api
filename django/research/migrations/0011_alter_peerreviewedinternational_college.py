# Generated by Django 3.2.5 on 2021-07-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0010_auto_20210703_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerreviewedinternational',
            name='college',
            field=models.CharField(choices=[('CBE', 'COLLEGE OF BUSINESS AND ECONOMY'), ('CST', 'COLLEGE OF SCIENCE AND TECHNOLOGY')], max_length=100),
        ),
    ]
