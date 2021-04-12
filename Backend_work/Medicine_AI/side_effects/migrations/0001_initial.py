# Generated by Django 2.2 on 2021-03-20 14:23

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='side_effects_data',
            fields=[
                ('alpha', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name_list', django_mysql.models.ListTextField(models.CharField(max_length=100), size=400)),
            ],
        ),
    ]
