# Generated by Django 3.1.7 on 2021-03-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('topic', models.CharField(choices=[('A', 'Symptom_checker'), ('B', 'Drugs A-Z'), ('C', 'Drugs by Condition'), ('D', 'Side Effects'), ('E', 'First Aid'), ('F', 'My Med List')], max_length=1)),
                ('Issue', models.TextField()),
            ],
        ),
    ]
