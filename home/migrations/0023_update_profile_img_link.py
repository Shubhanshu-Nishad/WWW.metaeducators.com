# Generated by Django 3.1 on 2021-05-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_update_profile_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_profile',
            name='img_link',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]
