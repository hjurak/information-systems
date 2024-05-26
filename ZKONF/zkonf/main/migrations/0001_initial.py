# Generated by Django 5.0.6 on 2024-05-22 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.conference')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.participant')),
            ],
        ),
        migrations.CreateModel(
            name='ScientificWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('year_of_publication', models.IntegerField()),
                ('areas', models.ManyToManyField(related_name='works', to='main.area')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='works',
            field=models.ManyToManyField(related_name='participants', to='main.scientificwork'),
        ),
    ]
