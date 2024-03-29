# Generated by Django 3.1 on 2020-08-28 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cont_edu_qul'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='donar',
            name='image',
        ),
        migrations.AddField(
            model_name='announcement',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donar',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
