# Generated by Django 3.1 on 2020-09-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0013_auto_20200913_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='number',
            field=models.IntegerField(default='0'),
        ),
    ]
