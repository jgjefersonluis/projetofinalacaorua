# Generated by Django 3.2.4 on 2021-06-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FaixaEtaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Saude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Substancias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
    ]
