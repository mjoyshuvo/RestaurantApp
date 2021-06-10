# Generated by Django 3.0.7 on 2021-06-10 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20210610_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='menu',
            name='updated_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='updated_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='result',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='result',
            name='updated_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
