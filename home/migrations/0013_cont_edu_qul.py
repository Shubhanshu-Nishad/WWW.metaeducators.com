# Generated by Django 3.1 on 2020-08-26 05:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_announcement_about_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='cont',
            name='edu_qul',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
