# Generated by Django 5.2 on 2025-05-11 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lotnisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='lotnisko.lotnisko'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='lotnisko.lotnisko'),
        ),
    ]
