# Generated by Django 3.1 on 2020-08-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200821_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=100)),
                ('customer_desc', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/customer')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
