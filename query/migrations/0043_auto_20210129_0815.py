# Generated by Django 3.1.5 on 2021-01-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0042_auto_20210128_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='class_day',
            field=models.DateField(default='2021-01-29'),
        ),
    ]
