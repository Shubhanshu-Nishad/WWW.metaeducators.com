# Generated by Django 3.1 on 2020-08-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_donar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar',
            name='image',
            field=models.ImageField(default='', upload_to='static/donars'),
        ),
    ]
