# Generated by Django 3.1.5 on 2021-01-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0011_auto_20210115_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacheruser',
            name='lastloginat',
            field=models.CharField(max_length=30),
        ),
    ]