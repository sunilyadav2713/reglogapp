# Generated by Django 5.0.4 on 2024-04-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='con',
            fields=[
                ('name1', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.CharField(max_length=50)),
            ],
        ),
    ]
