# Generated by Django 3.0.6 on 2021-03-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sismologico', '0005_auto_20210316_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sismo',
            name='data_estaciones',
            field=models.TextField(max_length=6144),
        ),
    ]
