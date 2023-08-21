# Generated by Django 3.2.8 on 2023-08-18 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Listing',
        ),
        migrations.RemoveField(
            model_name='band',
            name='active',
        ),
        migrations.RemoveField(
            model_name='band',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='band',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='band',
            name='official_homepage',
        ),
        migrations.RemoveField(
            model_name='band',
            name='year_formed',
        ),
    ]
