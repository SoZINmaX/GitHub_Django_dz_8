# Generated by Django 4.0.6 on 2022-07-23 11:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_date_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='movies',
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None, verbose_name='genres'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_adult',
            field=models.BooleanField(default=False, verbose_name='isAdult'),
        ),
        migrations.AlterField(
            model_name='person',
            name='imdb_id',
            field=models.CharField(max_length=255, verbose_name='nconst'),
        ),
        migrations.AlterField(
            model_name='personmovie',
            name='order',
            field=models.IntegerField(null=True, verbose_name='ordering'),
        ),
    ]
