# Generated by Django 3.2.8 on 2023-08-18 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0002_delete_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5)),
                ('biography', models.CharField(max_length=100)),
                ('year_formed', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
                ('active', models.BooleanField(default=True)),
                ('official_homepage', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
