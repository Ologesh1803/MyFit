# Generated by Django 5.1.4 on 2024-12-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('primary_muscle', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vegetarian', models.BooleanField()),
                ('ready_mins', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
    ]
