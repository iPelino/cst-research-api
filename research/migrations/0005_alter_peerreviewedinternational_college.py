# Generated by Django 3.2.3 on 2021-06-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_alter_peerreviewedinternational_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerreviewedinternational',
            name='college',
            field=models.CharField(choices=[('CST', 'COLLEGE OF SCIENCE AND TECHNOLOGY'), ('CBE', 'COLLEGE OF BUSINESS AND ECONOMY')], max_length=100),
        ),
    ]
