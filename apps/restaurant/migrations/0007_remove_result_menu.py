# Generated by Django 3.0.7 on 2021-06-08 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20210607_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='menu',
        ),
    ]
