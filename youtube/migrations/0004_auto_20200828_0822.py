# Generated by Django 3.1 on 2020-08-28 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_auto_20200825_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
        migrations.AddField(
            model_name='video',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
