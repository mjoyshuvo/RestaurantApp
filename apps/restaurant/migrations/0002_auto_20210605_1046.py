# Generated by Django 3.0.7 on 2021-06-05 10:46

import conf.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.FileField(upload_to='menus', validators=[conf.validators.validate_file_extension_menu]),
        ),
    ]