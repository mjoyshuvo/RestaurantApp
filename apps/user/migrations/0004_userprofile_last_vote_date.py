# Generated by Django 3.0.7 on 2021-06-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_vote_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]