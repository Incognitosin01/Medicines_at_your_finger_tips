# Generated by Django 3.1.7 on 2021-03-19 19:26

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine_data',
            fields=[
                ('alpha', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name_list', django_mysql.models.ListTextField(models.CharField(max_length=100), size=400)),
            ],
        ),
    ]
