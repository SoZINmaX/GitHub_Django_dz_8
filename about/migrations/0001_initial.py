# Generated by Django 4.0.6 on 2022-07-18 22:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutmyself',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('datetimenow', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
