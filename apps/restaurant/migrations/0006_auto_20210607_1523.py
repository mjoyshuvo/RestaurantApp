# Generated by Django 3.0.7 on 2021-06-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_vote_vote_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.AddField(
            model_name='result',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Menu'),
        ),
        migrations.AddField(
            model_name='result',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_restaurant', to='restaurant.Restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('restaurant', 'created_at')},
        ),
    ]